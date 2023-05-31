#!/usr/bin/python3
""""
This is python script that starts a Flask web application
The app is  listening on 0.0.0.0, port 5000
route:
    /states: List all states
    /states/<id>: List the state and cities in the state or Not Found
"""
from flask import Flask, render_template
from models import storage
from models.state import State
import os

app = Flask(__name__)


@app.teardown_appcontext
def close_app(error):
    """ After each request removes the current SQLAlchemy Session. """
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """ List all states in the DB. """

    all_states = storage.all(State).values()
    sorted_state = sorted(all_states, key=lambda key: key.name)
    return render_template('9-states.html', states=sorted_state)


@app.route('/states/<id>', strict_slashes=False)
def single_state(id):
    """ Renders a single State and All the cities in the State. """

    all_state = storage.all(State).values()
    found = 0
    state = None
    for item in all_state:
        if item.id == id:
            state = item
            found = 1
    return render_template('9-states.html', states=state, found=found)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', '5000'))
    app.run(host='0.0.0.0', port=port)
