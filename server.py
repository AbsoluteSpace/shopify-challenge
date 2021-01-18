from flask import Flask, render_template
from knn import KNN
import sqlite3 as sql
import pandas as pd
import numpy as np
import os,sys

app = Flask(__name__)

def switch(x):
    return {
        'Normal': 0,
        'Fighting': 1,
        'Flying': 2,
        'Poison': 3,
        'Ground': 4,
        'Rock': 5,
        'Bug': 6,
        'Ghost': 7,
        'Steel': 8,
        'Fire': 9,
        'Water': 10,
        'Grass': 11,
        'Electric': 12,
        'Psychic': 13,
        'Ice': 14,
        'Dragon': 15,
        'Dark': 16,
        'Fairy': 17,
        'None': 18,
    }[x]

def get_cursor():
    conn = sql.connect("database.db")
    cur = conn.cursor()
    return (cur, conn)

"""Initialize the sqlite database and fill up the `pokemon` table with sample data."""
def initialize_db():
    (cur, conn) = get_cursor()

    cur.execute("DROP TABLE IF EXISTS pokemon")
    cur.execute("CREATE TABLE pokemon (name TEXT, type1 TEXT, type2 TEXT, imgpath TEXT)")

    folder = './static/images/'
    for filename in os.listdir(folder):
           infilename = os.path.join(folder,filename)
           if not os.path.isfile(infilename): continue
           oldbase = os.path.splitext(filename)
           newname = infilename.replace('.jpg', '.png')
           output = os.rename(infilename, newname)

    pokemon_df = pd.read_csv('./static/pokemon.csv')
    for p in pokemon_df.to_numpy():
        if not isinstance(p[2], str):
            p[-1] = 'None'
        data = (p[0], p[1], p[2], p[0] + '.png')
        cur.execute("INSERT INTO pokemon (name, type1, type2, imgpath) VALUES (?, ?, ?, ?)", data)

    conn.commit()

@app.route("/")
def home_page():
    (cur, _) = get_cursor()
    cur.execute("SELECT rowid, * FROM pokemon")
    
    rows = cur.fetchall()
    # TODO don't show all rows, just fetch like 9 or however many classes - or paginate it

    pokemons = []
    for row in rows[0:9]:
        pokemons.append({
            "id":    row[0],
            "name":  row[1],
            "src":   "static/images/%s" % (row[4]),
            "type1": row[2],
            "type2": row[3],
        })

    return render_template("index.html", pokemons=pokemons)

@app.route("/similar/<pokemon_id>")
def similar(pokemon_id):

    if not pokemon_id:
        return render_template("similar.html", pokemons=[])

    (cur, conn) = get_cursor()

    cur.execute("SELECT rowid, * FROM pokemon WHERE rowid = ?", (pokemon_id,))
    result = cur.fetchone()
    (rowid, name, type1, type2, imgpath) = result

    # TODO add the similar pokemon here
    cur.execute("SELECT rowid, * FROM pokemon")
    rows = cur.fetchall()

    # print(np.asarray(rows)[:,2:-1])

    new_arr = []
    y = []

    for p in rows:
        p_row = np.zeros(19)
        # print(switch(p[1]))
        p_row[switch(p[2])] = 1
        p_row[switch(p[3])] = 1
        # np.array(p_row)[19] = p['rowid']
        new_arr.append(p_row)
        # y.append(p[0])
        y.append(p)

    test = []
    new_res = np.zeros(19)
    new_res[switch(result[2])] = 1
    new_res[switch(result[3])] = 1
    test.append(new_res)

    # pokemon_df = pd.read_csv('./static/pokemon.csv')
    # for p in pokemon_df.to_numpy():
    #     if not isinstance(p[2], str):
    #         p[-1] = 'None'
    #     data = (p[0], p[1], p[2], p[0] + '.png')
    #     cur.execute("INSERT INTO pokemon (name, type1, type2, imgpath) VALUES (?, ?, ?, ?)", data)

    # print(np.asarray(test))

    model = KNN(6)
    model.fit(np.asarray(new_arr), np.asarray(y))
    y_pred = model.predict(np.asarray(test))

    # TODO grab more and randomly show 5?
    pokemons = []
    for row in y_pred[1:]:
        pokemons.append({
            "id":    row[0],
            "name":  row[1],
            "src":   "../static/images/%s" % (row[4]),
            "type1": row[2],
            "type2": row[3],
        })

    return render_template("similar.html", pokemons=pokemons)
    # TODO this is where I need something for similar items
    
if __name__ == '__main__':
    initialize_db()
    app.run(debug = True)