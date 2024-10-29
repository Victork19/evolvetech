from createDB import db

class User(db.Model):
    id = db.Column(db.Interger, primary_key=True)
    fist_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    receive_updates = db.Column(db.Boolean, default=False)
