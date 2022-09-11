from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.controllers import users_controller, recipes_controller, category_controller, ingredients_controller
from flask_app.models.users import User
from flask_app.models.recipes import Recipes
from flask_app.models.category import Category 
from flask_app.models.ingredients import Ingredient

@app.route('/create_ingredients')
def create_ingredientes():
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/')

    return render_template('/save_ingredients.html')

    

@app.route('/save_ingredients', methods=['POST'])
def save_ingredients():
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesión
        return redirect('/')

    if not Ingredient.valida_ingredientes(request.form): 
        return redirect('create/ingredients')

    Ingredient.save(request.form)

    return redirect('/dashboard/0')

@app.route('/view/ingredients') 
def view_ingredients():
    if 'user_id' not in session:  
        return redirect('/')
    formulario = {
        "id": session['user_id']
    }
    user = User.get_by_id(formulario) 
    ingredients = Ingredient.get_all()

    return render_template('view_ingredients.html', User=User, ingredients = ingredients)


@app.route('/edit/ingredients/<int:ingredient_id>') 
def edit_ingredients(ingredient_id):

    if 'user_id' not in session:  
        return redirect('/')

    formulario = {
        "id": session['user_id']
    }

    id = ingredient_id

    user = User.get_by_id(formulario) 
    ingredients = Ingredient.get_all(id)

    return render_template('edit_ingredients.html', User=User, ingredients = ingredients)


