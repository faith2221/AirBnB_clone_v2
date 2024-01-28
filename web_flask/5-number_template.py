#!/usr/bin/python3
"""
Starts a simple Flask web application.
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """
    Returns a given string.
    """
    return ('Hello HBNB!')


@app.route('/hbnb')
def hbnb():
    """
    It returns the string HBNB.
    """
    return 'HBNB'


@app.route('/c/<text>')
def Ctext(text):
    """
    Displays “C” followed by the value of the text variable.
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """
    Text python is cool'
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>')
def print_int(n):
    """
    Displays n is a number.
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def num_template(n):
    """
    It retrieves  the template request.
    """
    path = '5-number.html'
    return render_template(path, n=n)


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
