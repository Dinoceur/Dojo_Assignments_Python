from flask_app import app
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)
from flask import render_template,redirect,request,session,flash
from flask_app.models.user_model import User


@app.route('/')
def index():
    return render_template('login_registration.html')

@app.route('/welcome')
def welcome():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template('welcome.html', users = User.get_by_id(data))

@app.post('/register')
def user():
    if not User.validate_registration(request.form):
        return redirect('/')
    # if not User.validate_user(request.form):
    #     return redirect('/')
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(data)
    session['user_id'] = id
    
    return redirect('/welcome')

@app.post('/login')
def login():

    users_in_db = User.get_by_email(request.form)
    if not users_in_db:
        flash("Invalid Email/Password","login")
        return redirect("/")
    if not bcrypt.check_password_hash(users_in_db.password, request.form['password']):
        flash("Invalid Email/Password","login")
        return redirect('/')
    session['user_id'] = users_in_db.id
    return redirect("/welcome")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
