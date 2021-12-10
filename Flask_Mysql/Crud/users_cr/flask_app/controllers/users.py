from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/users')


@app.route('/users')
def users():
    return render_template("read.html",users=User.get_all())


@app.route('/user/new')
def new():
    return render_template("create.html")

@app.post('/user/create')
def create():
    user_id = User.save(request.form)
    return redirect(f'/user/show/{user_id}')

@app.route('/user/edit/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("edit.html",user=User.get_one(data))

@app.route('/user/show/<int:id>')
def show(id):
    data ={
        'id':id
    }
    return render_template('show.html',user=User.get_one(data))

@app.post('/user/update/<int:id>')
def update(id):
    data ={ 
        **request.form,
        "id":id
    }
    User.update(data)
    return redirect(f'/user/show/{id}')

@app.route('/user/delete/<int:id>')
def delete(id):
    data ={
        'id':id
    }
    User.delete(data)
    return redirect('/users')


