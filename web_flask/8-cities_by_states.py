#!/usr/bin/python3
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def tear_down_app_context(error):
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    all_states = storage.all('State')
    return render_template('8-cities_by_states.html', all_states=all_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
