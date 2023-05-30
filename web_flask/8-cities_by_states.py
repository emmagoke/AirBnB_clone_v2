#!/usr/bin/python3
"""
This is python script that starts a Flask web application
The app is  listening on 0.0.0.0, port 5000
route: /cities_by_states -> List State and City in those state.
"""
from flask import Flask, render_template
from models.state import State
from models import storage
import os

app = Flask(__name__)


@app.teardown_appcontext
def close_app(error):
    """ After each request removes the current SQLAlchemy Session. """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_state():
    """ Returns all state object sorted by name. """

    all_state = storage.all(State).values()
    sorted_state = sorted(all_state, key=lambda key: key.name)
    return render_template('8-cities_by_states.html', states=sorted_state)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', '5000'))
    app.run(host='0.0.0.0', port=port)
