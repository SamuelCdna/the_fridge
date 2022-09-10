from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.controllers import users_controller ,recipes_controller
from flask_app.models.users import User
from flask_app.models.recipes import Recipes
from flask_app.models.category import Category 
from flask_app.models.ingredients import Ingredient


@app.route('/save/ingredients')
def new_ingredients():
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesión
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario) #Instancia del usuario que inicio sesión

    return render_template('save_ingredients.html', user=user)

@app.route('/create_ingredients', methods=['POST'])
def create_ingredientes():
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/')

    if not Ingredient.valid_ingredients(request.form): #llama a la función de valida_receta enviándole el formulario, comprueba que sea valido 
        return redirect('save/ingredients')

    Ingredient.save(request.form)

    return redirect('/dashboard')

@app.route('/edit/ingredient/<int:id>') #a través de la URL recibimos el ID de la receta
def edit_ingredient(id):
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario) #Instancia del usuario que inicio sesión

    #La instancia de la receta que queremos editar
    formulario_receta = {"id": id}
    ingredient = Ingredient.get_by_id(formulario_receta)

    return render_template('ingredients.html', user=user, ingredient=ingredient)


@app.route('/delete/ingredient/<int:id>')
def delete_ingredient(id):
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    
    formulario = {"id": id}
    Ingredient.delete(formulario)

    return redirect('/dashboard')


