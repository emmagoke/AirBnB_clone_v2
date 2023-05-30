#!/usr/bin/python3
"""
This is python script that starts a Flask web application
The app is listening on 0.0.0.0, port 5000
route: /cities_by_states -> Render an html page with the
state id and state names
"""
from flask import Flask, render_template
from os import getenv
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_appp():
    """ After each request you removes the current SQLAlchemy Session. """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Gets and displays all the State in the DB. """

    state_list = storage.all(State).values()
    return render_template('7-states_list.html', states=state_list)

if __name__ == '__main__':
    port = int(getenv('PORT'))
    app.run(host='0.0.0.0', port=port)
