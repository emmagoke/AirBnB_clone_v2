#!/usr/bin/python3
"""
This python script starts a Flask web application tht diplays “Hello HBNB!”
at /
"""
import os
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """ The home page route"""
    return "Hello HBNB!"


port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
