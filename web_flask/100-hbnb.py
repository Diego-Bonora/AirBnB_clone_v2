#!/usr/bin/python3
""" first flask web app """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User
from markupsafe import Markup

app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage(e):
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def states_list():
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    users = storage.all(User)
    for place in places.values():
        place.description = Markup(place.description)
    return render_template('100-hbnb.html', states=states, amenities=amenities, places=places, users=users)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
