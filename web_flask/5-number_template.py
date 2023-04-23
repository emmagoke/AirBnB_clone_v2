#!/usr/bin/python3
"""
This is python script that starts a Flask web application
The app is  listening on 0.0.0.0, port 5000
Routes:

    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
"""
import os
from flask import Flask, render_template
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


@app.route('/python', strict_slashes=False)
@app.route('/python/<path:text>', strict_slashes=False)
def python_text(text=None):
    """ This /python or /python/text route."""
    if text is None:
        return 'Python is cool'
    elif '_' in text:
        text = text.replace('_', ' ')

    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ This is number/anynumber route. """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ This route an html template with n in the body tag. """
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
