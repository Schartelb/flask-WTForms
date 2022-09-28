from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional


class AddPetForm(FlaskForm):
    """Form for adding/editing pets."""

    name = StringField("Name",
                       validators=[InputRequired(message="Name is required")])
    species = StringField("Species",
                          validators=[InputRequired(message='What species is it?')])
    photo_url = StringField("Photo URL", validators=[Optional()])
    age = IntegerField("Age", validators=[Optional()])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Available",
                             default='checked',
                             validators=[InputRequired(message="Is it adoptable?")])
