from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.controllers import users_controller ,recipes_controller, category_controller, ingredients_controller
from flask_app.models.users import User
from flask_app.models.recipes import Recipes
from flask_app.models.category import Category
from flask_app.models.ingredients import Ingredient

@app.route('/create/category')
def createcategory():

    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/')
        
    return render_template('save_category.html')

@app.route('/save_category', methods=['POST'])
def save_category():
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/')

    if not Category.valida_categoria(request.form): #llama a la función de valida_receta enviándole el formulario, comprueba que sea valido 
        return redirect('/create/category')

    Category.save(request.form)

    return redirect('/dashboard')