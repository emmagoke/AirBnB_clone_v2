#!/usr/bin/python3
"""
This is python script that starts a Flask web application
The app is  listening on 0.0.0.0, port 5000
Routes:

    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
"""
import os
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """ The home page route. """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ This is the hbnb route. """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    if '_' in text:
        text = text.replace('_', ' ')

    return "C {}".format(text)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
