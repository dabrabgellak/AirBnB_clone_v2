#!/usr/bin/python3
from flask import Flask, request

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Starts a Flask web application """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """  """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """  """
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', defaults={"text": "is_cool"})
@app.route("/python/<text>", strict_slashes=False)
def python_iscool(text):
    """  """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
        Display - n is a number
        Return - n if n is an integer.
    """
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
