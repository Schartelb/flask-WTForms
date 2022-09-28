from flask import Flask, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

from forms import AddPetForm

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
    return render_template('home.html')


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Pet add form; handle adding."""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        pet = Pet(name=name,
                  species=form.species.data,
                  photo_url=form.photo_url.data,
                  age=form.age.data,
                  notes=form.notes.data,
                  available=form.notes.data)
        db.session.add(pet)
        db.session.commit()
        flash(f"Added {name} to adoption list!")
        return redirect("/")
    else:
        return render_template(
            "addpet.html", form=form)


@app.route("/<int:pet_id>", methods=["GET"])
def display_pet(pet_id):
    return render_template("displaypet.html")
