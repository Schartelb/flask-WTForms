from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional

species = [('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')]


class PetForm(FlaskForm):
    """Form for adding/editing pets."""

    name = StringField("Name",
                       validators=[InputRequired(message="Name is required")])
    species = SelectField("Species", choices=species,
                          validators=[InputRequired(message='What species is it?')])
    photo_url = StringField("Photo URL", validators=[Optional()])
    age = IntegerField("Age", validators=[Optional()])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Available",
                             default='checked')
