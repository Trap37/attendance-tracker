from typing import Any

from flask import redirect, render_template, url_for

from server import app
from server.forms import ScanForm, StudentRegistrationModalForm

# TODO:: scan_log must be populated with today's scans via Attendance model query
scan_log: list[Any] = []


@app.route('/')
def index():
    scan_form = ScanForm()
    registration_form = StudentRegistrationModalForm()
    # FIXME:: Do I need this?
    tabs = [
        {'id': 'attendance', 'label': 'Attendance'},
        {'id': 'gear', 'label': 'Gear Checkout'},
        {'id': 'history', 'label': 'History'},
        {'id': 'students', 'label': 'Students'},
        {'id': 'reports', 'label': 'Reports'},
    ]

    return render_template(
        'index.html.j2',
        scan_form=scan_form,
        registration_form=registration_form,
        tabs=tabs,
        scan_log=scan_log,
    )


@app.post('/log_visit')
def log_visit():
    # TODO: Implement logic to log a student's visit
    return '', 204


@app.post('/register_student')
def register_student():
    scan_form = ScanForm()
    registration_form = StudentRegistrationModalForm()

    # Identify if cancel button was pushed
    if registration_form.cancel.data:
        # IDEA: Can use javascript to avoid page reloading
        # Can instead just hide modal
        return redirect(url_for('index'))

    if registration_form.validate_on_submit():
        # TODO: Implement logic to register a new student
        # TODO: Return a success popup message with alert() in html/javascript
        return redirect(url_for('index'))

    return render_template(
        'index.html.j2', scan_form=scan_form, registration_form=registration_form
    )
