from typing import Any

from flask import redirect, render_template, url_for

from server import app
from server.dto import GearStats
from server.forms import (
    AttendanceHistoryCardForm,
    ScanForm,
    StudentRegistrationModalForm,
)

# TODO:: scan_log must be populated with today's scans via Attendance model query
# TODO: Can maybe do something similar to what I did with GearStats class so this isn't here
scan_log: list[Any] = []


@app.route('/')
@app.route('/index')
def index():
    scan_form = ScanForm()
    registration_form = StudentRegistrationModalForm()
    # FIXME:: Do I need this?
    # tabs = [
    #     {'id': 'attendance', 'label': 'Attendance'},
    #     {'id': 'gear', 'label': 'Gear Checkout'},
    #     {'id': 'history', 'label': 'History'},
    #     {'id': 'students', 'label': 'Students'},
    #     {'id': 'reports', 'label': 'Reports'},
    # ]
    attendance_history_form = AttendanceHistoryCardForm()

    return render_template(
        'index.html.j2',
        scan_form=scan_form,
        registration_form=registration_form,
        # tabs=tabs,
        scan_log=scan_log,
        gear_stats=GearStats.stats(),
        gear_checkouts=GearStats.checkouts(),
        attendance_history_form=attendance_history_form,
    )


@app.post('/log_visit')
def log_visit():
    # TODO: Implement logic to log a student's visit
    return '', 204


# See app.py #136 for reference code
def _parse_date(date_str: str) -> Any: ...


@app.post('/attendance_history')
def attendance_history():
    form = AttendanceHistoryCardForm()

    history_records = {}
    start_date = form.start_date.default().strftime('%Y-%m-%d')
    end_date = form.end_date.default().strftime('%Y-%m-%d')

    if form.validate_on_submit():
        # TODO: Implement logic to retrieve attendance history
        # start_date = form.start_date.data
        # end_date = form.end_date.data

        # if start_date > end_date:
        #     flash("Start date cannot be after end date.", "error")
        # else:
        #     start_datetime = datetime.combine(start_date, time.min)
        #     end_datetime = datetime.combine(
        #         end_date + timedelta(days=1),
        #         time.min
        #     )

        #     history_records = (
        #         Attendance.query
        #         .filter(
        #             Attendance.timestamp >= start_datetime,
        #             Attendance.timestamp < end_datetime
        #         )
        #         .order_by(Attendance.timestamp.desc())
        #         .all()
        #     )
        history_records = {
            'start': '2026-10-01',
            'end': '2026-10-19',
            'count': 2,
            'rows': [
                {
                    'check_in_time': '2026-10-15 08:30:00',
                    'day_of_week': 'Thursday',
                    'scanner_code': '40921',
                    'school_id': '2910287',
                    'full_name': 'Alex Smith',
                    'major': 'Business',
                    'grade_level': 'null',
                },
                {
                    'check_in_time': '2026-10-16 09:00:00',
                    'day_of_week': 'Friday',
                    'scanner_code': '18203',
                    'school_id': '2910288',
                    'full_name': 'Jamie Lee',
                    'major': 'Computer Science',
                    'grade_level': 'Senior',
                },
            ],
        }

    return render_template(
        'index.html.j2',
        attendance_history_form=form,
        history_records_data=history_records,
        history_start_date=start_date,
        history_end_date=end_date,
        scan_form=ScanForm(),
        registration_form=StudentRegistrationModalForm(),
        gear_stats=GearStats.stats(),
        gear_checkouts=GearStats.checkouts(),
    )


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
