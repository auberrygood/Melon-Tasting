"""CRUD operations."""

from model import db, User, Appointment, connect_to_db
import requests
import os

all_time_slots = ['00:00:00', '00:30:00', '01:30:00', '02:00:00', '02:30:00', '03:00:00', '03:30:00', 
            '04:00:00', '04:30:00', '05:00:00', '05:30:00', '06:00:00','06:30:00', '07:00:00', 
            '07:30:00', '08:00:00', '08:30:00', '09:00:00', '09:30:00', '10:00:00', '10:30:00', 
            '11:00:00', '11:30:00', '12:00:00', '12:30:00', '13:00:00', '13:30:00', '14:00:00', 
            '14:30:00', '15:00:00', '15:30:00', '16:00:00', '16:30:00', '17:00:00', '17:30:00', 
            '18:00:00', '18:30:00', '19:00:00', '19:30:00', '20:00:00', '20:30:00', '21:00:00', 
            '21:30:00', '22:00:00', '22:30:00', '23:00:00', '23:30:00']

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

"""****************** APPOINTMENT FUNCTIONS *****************"""

def book_appt(user_id, date, starttime):
    """ Create and return a booked appointment """
    appointment = Appointment(id=user_id, date=date, starttime=starttime)

    db.session.add(appointment)
    db.session.commit()

    return appointment

def show_appointments_by_user(user_id):
    """Return all appointments booked by user"""
    user_appointments = Appointment.query.filter_by(id=user_id).all()
    
    return user_appointments

def show_all_booked_appointments_by_day(date):
    """Return all appointments booked"""
    all_booked_appointments_by_day = Appointment.query.filter_by(date=date).all()

    return all_booked_appointments_by_day

def show_appontments_by_user_and_day(user_id, date):
    """Return all appointments booked by a user on a specific day"""
    user_appointments_by_day = Appointment.query.filter_by(id=user_id, date=date).all()

    return user_appointments_by_day

def show_available_appointments_by_date(date):
    available_appointments=all_time_slots
    booked_appointments = Appointment.query.filter_by(date=date).all()
    # import pdb
    # pdb.set_trace()
    print("*************************")
    print(booked_appointments)
    print("*************************")
    if len(booked_appointments):
        for appt in booked_appointments:
            for time in available_appointments:
                if appt.starttime == time:
                    available_appointments.remove(time)
        print("*************************")
        print(available_appointments)
        print("*************************")
        return available_appointments
    return all_time_slots
    
    
