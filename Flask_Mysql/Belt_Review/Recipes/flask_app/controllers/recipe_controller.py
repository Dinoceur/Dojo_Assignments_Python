from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.recipe_model import Recipe
from flask_app.models.user_model import User

@app.route('/')
def index():
    render_template('recipes.html')

@app.route('/dashboard')
def welcome():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={ 
        "user":User.get_by_id(id=session['user_id']),
        "recipes": Recipe.get_all()
    }
    return render_template('dashboard.html',**data)

@app.route('/recipes/new')
def new():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template("recipe_new.html")

@app.post('/add')
def add():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
    data ={
        **request.form,
        'user_id':session['user_id']
    }
    Recipe.save(data)
    return redirect('/dashboard')

@app.route('/recipes/edit/<int:id>')
def edit(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={ 
        "user":User.get_by_id(id=session['user_id']),
        "recipe": Recipe.get_one(id=id)
    }
    return render_template("recipe_edit.html", **data)

@app.post('/update/<int:id>')
def update(id):
    if 'user_id' not in session:
        return redirect('/logout')
    if not Recipe.validate_recipe(request.form):
        return redirect(f'/recipes/edit/{id}')
    data ={
        **request.form,
        'id':id
    }
    Recipe.update(data)
    return redirect('/dashboard')

@app.route('/instructions/<int:id>')
def view(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={ 
        "user":User.get_by_id(id=session['user_id']),
        "recipe": Recipe.get_one(id=id)
    }
    return render_template("recipe.html", **data)

@app.route('/recipes/delete/<int:id>')
def delete(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id':id
    }
    Recipe.delete(data)
    return redirect('/dashboard')