from flask_app import app
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)
from flask import render_template,redirect,request,session,flash
from flask_app.models.registration_model import Register


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
    return render_template('welcome.html', register = Register.get_by_id(data))

@app.post('/register')
def register():
    if not Register.validate_registration(request.form):
        return redirect('/')
    if not Register.validate_user(request.form):
        return redirect('/')
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = Register.save(data)
    session['user_id'] = id
    
    return redirect('/welcome')

@app.post('/login')
def login():

    register_in_db = Register.get_by_email(request.form)
    if not register_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(register_in_db.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/')
    session['user_id'] = register_in_db.id
    return redirect("/welcome")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
