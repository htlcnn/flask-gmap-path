from flask import Flask, render_template
from flask_bootstrap import Bootstrap

import json
import datetime

import requests

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    with open('logs.json') as f:
        logs = json.load(f)
    logs = [log[:-1] for log in logs]
    return render_template('index.html', data=logs, coords=[])


@app.route('/path/<vid>/<depart_time>')
def path(vid, depart_time):
    with open('logs.json') as f:
        logs = json.load(f)
    coords = []
    for log in logs:
        if log[1] == vid and log[2] == depart_time:
            coords = log[3]

    return render_template('index.html', data=[log[:-1] for log in logs],
                            coords=coords, vid=vid, depart_time=depart_time)


if __name__=='__main__':
    app.run(debug=True)
