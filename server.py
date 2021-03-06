"""Server for Melon Tasting app."""

from model import connect_to_db
from model import User
from flask import Flask, render_template, request, flash, session, redirect, jsonify
import crud
import os
import requests
import json
from datetime import date
from jinja2 import StrictUndefined
from flask_login import LoginManager, current_user, login_user, logout_user, login_required

app = Flask(__name__)
app.secret_key = "melon"
app.jinja_env.undefined = StrictUndefined

login_manager = LoginManager(app)
login_manager.login_view = '/'


"""************* LOG IN / LOG OUT *************"""
@app.route('/')
def login_page():
    """ Show login page"""
    if current_user.is_authenticated:
        return redirect('/appointmentsearch')

    return render_template('login-page.html')


@login_manager.user_loader
def load_user(id):
    """ Flask-Login function to retrieve ID of user from session if any, and load user into memory """
    user = User.query.filter_by(id=id).first()
    
    return user
    

@app.route('/login', methods = ['GET', 'POST'])
def login():
    """ Log user in and add user info to session """

    if current_user.is_authenticated:
        return redirect('/appointmentsearch')
        
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)
    print("**********")
    print(user)
    print("**********")
    
    if user:
        if user.check_password(password)==True:
            login_user(user)
            # flash('Login Successful')
            return redirect('/appointmentsearch')
        else:
            flash('Invalid password.')
            return redirect('/')
    else:
        flash('Sorry, this user does not exist.')
        return redirect('/')

@app.route('/newaccount')
def new_account_page():
    """ Show create account page"""
    return render_template('create-account.html')

@app.route('/create/user', methods = ['POST'])
def create_login():
    """ Create login credentials for user """

    user_email = request.form.get('email')
    print(user_email)
    user_name = request.form.get('name')
    print(user_name)
    user_password = request.form.get('password')
    print(user_password)

    potential_user = crud.get_user_by_email(user_email)

    if potential_user != None:
        flash('Email already in use, please use a different email.')
        return redirect('/newaccount')
    else:
        crud.create_user(name=user_name, email=user_email, password=user_password)
        flash('New account created! You may now log in.')
        return redirect('/')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Successfully logged out')
    return redirect('/')

@app.route('/appointmentsearch')
def calendar_page():
    """ Show appointment search by calendar page"""
    return render_template('appointment-search.html',
                            apptdate=date)

@app.route('/appointmentresults', methods=['GET'])
def time_page():
    """Show available appointment times"""
    appointment_day = request.args.get('appointment-day')
    available_appointments = crud.show_available_appointments_by_date(appointment_day)
    # check if user already has appointment scheduled on appointment day
    user_appointments_on_day = crud.show_appontments_by_user_and_day(user_id=current_user.id, date=appointment_day)
    if user_appointments_on_day:
        flash("#TooMuchMelon! You already have an appointment on that day, please choose another date.")
        return redirect ('/appointmentsearch')

    else:
        return render_template('time-results.html',
                            appointment_day=appointment_day,
                            available_appointments=available_appointments)

@app.route('/bookappointment/<appointment_day>', methods = ['POST'])
def book_appointment(appointment_day):
    """book appointment, store in database"""
    # grab selected appointment time from form
    starttime = request.form.get('available-time-slots')
    print("********************")
    print(starttime)
    print("********************")
    # book appointment
    booked_appointment = crud.book_appt(user_id=current_user.id, date=appointment_day, starttime=starttime)

    return render_template('booking-confirmed.html')

@app.route('/confirmedappointments')
def confirmed_appt_page():
    """Show all user's booked appts"""
    appointments = crud.show_appointments_by_user(current_user.id)
    return render_template('confirmed-appointments.html',
                            appointments=appointments)


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)