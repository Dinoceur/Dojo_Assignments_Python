from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.dojo_model import Dojo


@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    return render_template("create_dojo.html",dojos=Dojo.get_all())

@app.post('/dojos/create')
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def dojo_ninjas(id):
    data = {
            'id':id
    }
    return render_template("dojo_show.html",dojo=Dojo.get_one(data)) 
    
