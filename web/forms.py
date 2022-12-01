from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired
from wtforms.csrf.core import CSRF
from hashlib import md5
SECRET_KEY = '72109ede3972aab8'
class IPAddressCSRF(CSRF):
    """
    Generate a CSRF token based on the user's IP. I am probably not very
    secure, so don't use me.
    """
    def setup_form(self, form):
        self.csrf_context = form.meta.csrf_context
        return super(IPAddressCSRF, self).setup_form(form)

    def generate_csrf_token(self, csrf_token):
        token = md5(SECRET_KEY + self.csrf_context).hexdigest()
        return token

    def validate_csrf_token(self, form, field):
        if field.data != field.current_token:
            raise ValueError('Invalid CSRF')
class baseSecureForm(FlaskForm):
    class Meta:
        csrf = True;


class create_project_form(baseSecureForm):
    user_initials = StringField("User Initials", validators = [DataRequired()])
    event_name = StringField("Event Name", validators = [DataRequired()])
    can_connector_id = StringField("CAN Connector ID", validators=[DataRequired()])
    vehicle_id = StringField("Vehicle ID", validators=[DataRequired()])
    baud_rate = StringField("Baud Rate", validators=[DataRequired()])
    can_dbc= StringField("CAN DBC", validators=[DataRequired()])
    validators = [DataRequired()]
    submit = SubmitField("Submit")

class sync_form(baseSecureForm):
    submit = SubmitField("Submit")

class create_node(baseSecureForm):
    node_name = StringField("Node Name", validators=[DataRequired()])
    validators = [DataRequired()]
    submit = SubmitField("Submit")