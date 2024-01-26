#!/usr/bin/python3
"""
Starts a simple Flask web application.
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Returns a given string.
    """
    return ("Hello HBNB!")


@app.route('/', strict_slashes=False)
def hbnb():
    """
    Displays "Hello HBNB!" on the /hbnb path.
    """
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def display_ctext(text_to_display):
    """
    Displays “C” followed by the value of the text variable.
    """
    return "C {}".format(text_to_display.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
