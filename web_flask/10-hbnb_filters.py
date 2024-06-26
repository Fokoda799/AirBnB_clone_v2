#!/usr/bin/python3
"""starts a Flask web application for AirBnB clone"""

from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a HTML page of the States
    """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display a HTML page of States and their Cities
    """
    states = storage.all(State).values()
    cities = list()

    return render_template('8-cities_by_states.html',
                           states=states)


@app.route('/states', strict_slashes=False)
def states():
    """Display a HTML page of the States
    """
    states = storage.all(State)
    return render_template('7-states_list.html',
                           states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """ display a HTML page with State, Cities and
    City objects linked to the State.
    """
    states = storage.all(State).values()

    for state in states:
        if id == state.id:
            return render_template('9-states.html',
                                   states=states, state=state)

    return render_template('9-states.html', not_found=True)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """display a HTML page showing more styling
    """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    cities = list()

    for state in states:
        for city in state.cities:
            cities.append(city)

    return render_template('10-hbnb_filters.html',
                           states=states, state_cities=cities,
                           amenities=amenities)


@app.teardown_appcontext
def teardown_db_conn(error):
    """Closes the database again at the end of the request.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
