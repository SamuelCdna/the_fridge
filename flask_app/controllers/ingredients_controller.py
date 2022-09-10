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

    return render_template('/search_ingredients.html')

@app.route('/save_ingredients', methods=['POST'])
def save_ingredients():
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesión
        return redirect('/')

    if not Ingredient.valida_ingredientes(request.form): 
        return redirect('create/ingredients')

    Ingredient.save(request.form)

    return redirect('/dashboard')


