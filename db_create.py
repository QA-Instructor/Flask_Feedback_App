# from app import db

# db.create_all()

from app import db, app

with app.app_context():
    db.create_all()