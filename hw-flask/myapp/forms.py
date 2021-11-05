from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField

from wtforms.validators import DataRequired


class TopCities  (FlaskForm):
    """docstring for TopCities  ."""
    city_name = StringField(validators=[DataRequired()])
    city_rank = IntegerField(validators=[DataRequired()])
    is_visited = BooleanField()
    submit = SubmitField("Submit")
