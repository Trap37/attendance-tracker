
from flask import render_template

from attendance_tracker.server import app


@app.route('/')
def index():
    return render_template('index.html')
