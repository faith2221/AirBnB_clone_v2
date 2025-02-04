#!/usr/bin/python3
"""
Imports flask to run the web app.
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """
    Method used to close the session.
    """
    storage.close()


@app.route("/states", strict_slashes=False)
def state():
    """
    Displays an html page with States.
    """
    states = storage.all(State)
    return render_template("9-states.html", states=states, mode="all")


@app.route("/states/<id>", strict_slashes=False)
def state_by_id(id):
    """
    displays an html page with cities of that state.
    """
    for state in storage.all(State).values():
        if state.id == id:
            return render_template("9-states.html", state=state, mode="id")
    return render_template("9-states.html", state=None, mode="none")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
