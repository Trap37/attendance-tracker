from flask import Flask

app = Flask(__name__)

from attendance_tracker.server import routes
