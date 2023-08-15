#!/usr/bin/python3
""" first flask web app """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ First app rout for the proyect """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Second app rout for the proyect """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ third app rout for the proyect """
    text_no_underscore = text.replace("_", " ")
    return "C {}".format(text_no_underscore)


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python(text="is_cool"):
    """ fourth app rout for the proyect """
    text_no_underscore = text.replace("_", " ")
    return "Python {}".format(text_no_underscore)


@app.route('/number/<int:n>', strict_slashes=False)
def n(n):
    """ fifth app rout for the proyect """
    if n.isdigit():
        return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
