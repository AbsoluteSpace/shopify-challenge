# What is this

This is an image repository that recommends similar pokemon to the ones that you click on. It does this using the KNN Machine Learning algorithm with a pokemon's types as its features. There is an element of randomness in the recomendations to keep the similarity feature from becoming stale (for example if a pure grass type pokemon is recomended, there are so many pure grass types that the algorithm will soon only recommend them). The randomness is done just by grabbing some factor of nearest-neighbours more than we actually want to display, and then picking some at random.

Flask is used as a web application framework, and I chose it because it was quick and easy to use and can scale to complex applications.

SQLite is used because it was the simplest database for me to understand and store urls to pokemon images, their types, and their name. I did not store the pokemon images themselves in the database because of the large storage size requirement.


# Usage

This application requires [Flask](https://flask.palletsprojects.com/en/1.1.x/) which can be installed via pip.

It can be run by running `python server.py` from the project directory, at which point the user can navigate to the url that the terminal indicates to begin seeing similar pokemon.

## Troubleshooting

New to Flask? Try [this](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) tutorial, I found it helpful.

The `python` command is sometimes unrecognized but one of `python`, `python3`, `python2` usually works.


# Features I'd like to introduce

-  Pagination so that the initial pokemon recomendations aren't just the Kanto stater pokemon, and you could see more by selecting a page number on the bottom of the screen.
- Better random pokemon selections that not only allows for slightly different pokemon recommendations but also weights more similar pokemon with a higher probability of being displayed on screen. This could be done using `np.random.choice()`'s `p` parameter that allows you to include an array of probabilities.