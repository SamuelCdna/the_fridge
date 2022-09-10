from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.controllers import users_controller ,recipes_controller ,category_controller 
from flask_app.models.users import User
from flask_app.models.recipes import Recipes
from flask_app.models.category import Category 

@app.route('/create_ingredients', methods=['POST'])
def create_ingredientes():
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/')

    if not Recipe.valida_receta(request.form): #llama a la función de valida_receta enviándole el formulario, comprueba que sea valido 
        return redirect('save/ingredients')

    Recipe.save(request.form)

    return redirect('/dashboard')


