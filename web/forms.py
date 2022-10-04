from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class create_project_form(FlaskForm):
    user_initials = StringField("user initials", validators = [DataRequired()])
    event_name = StringField("event name", validators = [DataRequired()])
    can_connector_id = StringField("CAN connector ID", validators=[DataRequired()])
    vehicle_id = StringField("CAN connector ID", validators=[DataRequired()])
    baud_rate = StringField("baud rate", validators=[DataRequired()])
    can_dbc= StringField("CAN DBC", validators=[DataRequired()])
    validators = [DataRequired()]
    submit = SubmitField("manage-project")