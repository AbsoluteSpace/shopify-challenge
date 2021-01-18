# What is this

This is an image repository that recommends similar pokemon to the ones that you click on using the KNN Machine Learning algorithm with a pokemon's types as its features.

I have introduced an element of randomness in recommendations to keep the similarity feature from being stale (for example, due to the huge number of pure grass type pokemon, once one has been selected only pure grass types are recommended). The randomness is performed just by grabbing some number of nearest-neighbours that exceeds how many we actually want to display, and then picking some at random.

I chose to use python because I was really excited to try some machine learning based similarity recommendations and I have the most experience in this language for the limited time I had to work on this.

Flask is used as a web application framework, and I chose it because it was quick and easy to use and can scale to complex applications.

SQLite is used because it was the simplest database for me to understand. I store urls to pokemon images, their types, and their name. I did not store the pokemon images themselves in the database because of the large storage size requirement. This was based on the advice of [Microsoft](https://www.microsoft.com/en-us/research/publication/to-blob-or-not-to-blob-large-object-storage-in-a-database-or-a-filesystem/)


# Usage

This application requires [Flask](https://flask.palletsprojects.com/en/1.1.x/) which can be installed via pip.

It can be run by running `python server.py` from the project directory, at which point the user can navigate to the url that the terminal indicates to begin seeing similar pokemon.

## Troubleshooting

New to Flask? Try [this](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) tutorial, I found it helpful.

The `python` command is sometimes unrecognized but one of `python`, `python3`, `python2` usually works.


# Features I'd like to introduce

-  Pagination so that the initial pokemon recomendations aren't just the Kanto stater pokemon, and you could see more by selecting a page number on the bottom of the screen.
- Better random pokemon selections that not only allows for slightly different pokemon recommendations but also weights more similar pokemon with a higher probability of being displayed on screen. This could be done using `np.random.choice()`'s `p` parameter that allows you to include an array of probabilities.