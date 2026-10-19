from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired


class ScanForm(FlaskForm):
    scan_id = StringField('Scan ID', validators=[DataRequired()])
    submit = SubmitField('Scan')


class AttendanceHistoryCardForm(FlaskForm):
    start_date = StringField('Start Date', validators=[DataRequired()])
    end_date = StringField('End Date', validators=[DataRequired()])
    submit = SubmitField('Load')


class StudentRegistrationModalForm(FlaskForm):
    full_name = StringField(
        'Full Name', description='John Doe', validators=[DataRequired()]
    )
    csu_id = StringField('CSU ID', description='12345678', validators=[DataRequired()])
    scan_id = StringField(
        'Scan ID',
        description='5 Digit number on the back of ID',
        validators=[DataRequired()],
    )
    major = StringField(
        'Major', description='Computer Science', validators=[DataRequired()]
    )
    grade = SelectField(
        'Year',
        description='Freshman, Sophomore, etc.',
        choices=[
            ('', '-- Select year (optional) --'),
            ('Freshman', 'Freshman'),
            ('Sophomore', 'Sophomore'),
            ('Junior', 'Junior'),
            ('Senior', 'Senior'),
            ('Graduate', 'Graduate'),
        ],
        default='',
    )
    submit = SubmitField('Register')
    cancel = SubmitField('Cancel', render_kw={'formnovalidate': True})
