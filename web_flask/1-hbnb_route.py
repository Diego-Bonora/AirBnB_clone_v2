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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
