"""Models for Melon Tasting app."""

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()


class User(UserMixin, db.Model):
    """ A user."""

    __tablename__ = "users"

    id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True,
                        unique=True)

    name = db.Column(db.String(50),
                        unique=True)
    email = db.Column(db.String(120),
                        unique=True)
    password_hash = db.Column(db.String(130))

    #magic attributes:
        # appointments = a list of Appointment objects (name, appointment)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # def get_id(self):
    #     return unicode(self.id)

    def __repr__(self):
        return f'<User name: {self.name} email: {self.email} id: {self.id}>'


class Appointment(db.Model):
    """ A user's appointment. """
    
    __tablename__ = "appointments"

    appointment_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True)
    id = db.Column(db.Integer, 
                            db.ForeignKey('users.id'))
    date = db.Column(db.String)
    starttime = db.Column(db.String)

    #relationship tables:
    user = db.relationship("User",
                            backref="appointments")

    def __repr__(self):
        return f'<User: {self.user.name} Appointment: {self.date}, {self.starttime}>'


def connect_to_db(flask_app, db_uri='postgresql:///melontasting', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)