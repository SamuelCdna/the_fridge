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

    return render_template('save_ingredients.html')

@app.route('/save_ingredients', methods=['POST'])
def save_ingredients():
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesión
        return redirect('/')

    if not Ingredient.valida_ingredientes(request.form): 
        return redirect('/create_ingredients')

    Ingredient.save(request.form)

    return redirect('/ingredients')

@app.route('/ingredients')
def all_ingredients():
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesión
        return redirect('/')
    return render_template('all_ingredients.html', ingredients = Ingredient.get_all())


@app.route('/edit_ingredient/<int:id>') #a través de la URL recibimos el ID de la receta
def edit_ingredient(id):
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/')
    #La instancia de la receta que queremos editar
    return render_template('edit_ingredient.html', ingredient = Ingredient.get_by_id(id))

@app.route('/update_ingredients', methods=['POST'])
def update_ingredients():
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/')
    
    if not Ingredient.valida_ingredientes(request.form): 
        return redirect('/create_ingredients')
    Ingredient.update(request.form)
    return redirect('/ingredients')

@app.route('/delete_ingredient/<int:id>') #a través de la URL recibimos el ID de la receta
def delete_ingredient(id):
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/')
    Ingredient.delete(id)
    return redirect('/ingredients')


