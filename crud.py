"""CRUD operations."""

from model import db, User, Appointment, connect_to_db
import requests
import os


"""****************** USER FUNCTIONS *****************"""

def create_user(name, email, password):
    """ Create and return a user """
    user = User(name=name, email=email, password_hash=password)

    user.set_password(password)
    
    db.session.add(user)
    db.session.commit()

    return user


def show_all_users():
    """ Return a list of all user objects """
    users = User.query.all()
    
    return users


def get_user_by_email(email):
    """ Query for user by email """
    user = User.query.filter_by(email=email).first()
    if user:
        return user
    else:
        return None


def get_user_by_name(name):
    """ Query for user by user's name """
    user = User.query.filter_by(name=name).first()

    return user


def get_user_by_id(id):
    """ Query for user by id """
    user = User.query.filter(id=id).first()

    return user