#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask
from markupsafe import escape

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
    text = text.replace('_', ' ')
    return f'C {escape(text)}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
