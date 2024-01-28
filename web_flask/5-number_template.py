i#!/usr/bin/python3
"""
Starts a simple Flask web application.
"""
from flask import Flask, render template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Returns a given string.
    """
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Displays "Hello HBNB!" on the /hbnb path.
    """
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def Ctext(text):
    """
    Displays “C” followed by the value of the text variable.
    """
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonText(text="is cool"):
    """
    Displays python is cool.
    """
    return "Pyhton " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """
    Displays "n is a number" only if n is an integer.
    """
    if isinstance(n, int):
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n=None):
    """
    Displays an HTML page only if n is an integer.
    """
    if isinstance(n, int):
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run()
