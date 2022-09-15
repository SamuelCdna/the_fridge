from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.controllers import users_controller, recipes_controller, category_controller, ingredients_controller, reviews_controller
from flask_app.models.users import User
from flask_app.models.recipes import Recipes
from flask_app.models.category import Category 
from flask_app.models.ingredients import Ingredient
from flask_app.models.ingredient_receta import Ingrerecipe

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

    return redirect('/view/ingredients')

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
    return redirect('/view/ingredients')

@app.route('/delete_ingredient/<int:id>') #a través de la URL recibimos el ID de la receta
def delete_ingredient(id):
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/')
    Ingredient.delete(id)

    return redirect('/view/ingredients')











