#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Function that generates the main route """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """ Function that generates the /hbnb route """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hello_c(text):
    """ Function that generates the /c route """
    return f'C {escape(text)}'


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_python(text):
    """ This function generates the /python route """
    text_new = text.replace('_', ' ')
    return f'Python {escape(text_new)}'


@app.route('/number/<int:n>', strict_slashes=False)
def hello_int(n):
    """ This function generate the /number route """
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def html_body(n):
    """ This function generates the /number_template route """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    """ This function generates the /number_odd_or_even route """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
