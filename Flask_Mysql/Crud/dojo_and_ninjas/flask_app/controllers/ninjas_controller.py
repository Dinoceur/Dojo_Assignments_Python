from flask_app import app
from flask import render_template,redirect,request
from flask_app.models import ninja_model,dojo_model


@app.route('/ninjas')
def ninjas():
    return render_template("create_ninja.html",dojos= dojo_model.Dojo.get_all())

@app.post('/ninjas/create')
def create_ninja():
    ninja_model.Ninja.save(request.form)
    return redirect('/')
