from app import db
from models import Pet

db.drop_all()
db.create_all()

p = Pet(name="Aloysius",
        species="Porcupine",
        age=2,
        notes="prickly disposition",
        available=True)
db.session.add(p)
db.session.commit()
