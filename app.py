from flask import Flask, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

from forms import PetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///pet_adopt_db"
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)


@app.route("/")
def homepage():
    """Show pet's links."""
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Pet add form; handle adding."""

    form = PetForm()
    pet = {}
    if form.validate_on_submit():
        # for key, value in form.data.items():
        # Pet(key =value)
        pet = Pet(name=pet.name,
                  species=pet.species,
                  photo_url=pet.photo_url,
                  age=pet.age,
                  notes=pet.notes,
                  available=pet.available)
        db.session.add(pet)
        db.session.commit()
        flash(f"Added {pet.name} to adoption list!", "add")
        return redirect("/")
    else:
        return render_template(
            "addpet.html", form=form)


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def display_edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = PetForm(obj=pet)
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(f"Updated {pet.name}!", "update")
        return redirect(f"/{pet.id}")
    else:
        return render_template("displaypet.html", pet=pet, form=form)
