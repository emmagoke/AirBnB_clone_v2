#!/usr/bin/python3
"""
This is python script that starts a Flask web application
The app is  listening on 0.0.0.0, port 5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
import os

app = Flask(__name__)


@app.teardown_appcontext
def close_app(error):
    """ After each request removes the current SQLAlchemy Session. """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filter():
    """ Display all the state list and all amenities. """

    all_states = storage.all(State).values()
    sorted_state = sorted(all_states, key=lambda key: key.name)

    all_amenities = storage.all(Amenity).values()
    sorted_amenities = sorted(all_amenities, key=lambda key: key.name)

    return render_template('10-hbnb_filters.html', states=sorted_state,
                           amenities=sorted_amenities)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', '5000'))
    app.run(host='0.0.0.0', port=port)
