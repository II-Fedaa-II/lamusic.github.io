from musicPackage import db
# from werkzeug.security import generate_password_hash, check_password_hash



class User(db.Model):
        # __tablename__ = 'users'
    fname = db.Column(db.String(length=30),nullable=False)
    lname = db.Column(db.String(length=30),nullable=False)
    username = db.Column(db.String(length=16),nullable=False,unique=True)
    email = db.Column(db.String(length=40),nullable=False, primary_key = True)
    password = db.Column(db.String(length=15),nullable=False)
