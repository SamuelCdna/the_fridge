from flask import render_template, redirect, session, request, flash, jsonify
from flask_app import app

#Importación del modelo
from flask_app.models.users import User
from flask_app.models.recipes import Recipes
from flask_app.models.category import Category 
from flask_app.models.ingredients import Ingredient
from flask_app.models.ingredient_receta import Ingrerecipe
from flask_app.models.reviews import Reseñas
from flask_app.controllers import users_controller, recipes_controller, ingredients_controller, category_controller




@app.route ("/create/reseña" , methods=['POST'])
def createReseña():
    
    if not Reseñas.valida_reseña(request.form): 
        return redirect('/view_receta/'+ request.form['id'])

    if 'user_id' not in session:
        return redirect('/')

    Reseñas.save(request.form)
    return redirect('/view_receta/'+ request.form['recipe_id'])

@app.route('/delete/reseña/<int:id>')
def delete_reseña(id):
    if 'user_id' not in session: 
        return redirect('/')
    
    formulario = {"id": id}
    Reseñas.delete(formulario)
    return redirect('/dashboard/0')

@app.route('/edit/reseña/<int:id>') 
def edit_reseña(id):
    if 'user_id' not in session: 
        return redirect('/')
    formulario = {
        'id': session['user_id']
    }
    user = User.get_by_id(formulario) 
    formulario_reseña = {"id": id}
    reseña = Reseñas.get_by_id(formulario_reseña)
    recipes = Recipes.recipe_and_category()
    return render_template('edit_reseña.html', user=user, reseña=reseña, recipes=recipes)

@app.route('/update/reseña', methods=['POST'])
def update_res():
    if 'user_id' not in session: 
        return redirect('/')

    if not Reseñas.valida_reseña(request.form): 
        return redirect('/edit/reseña/'+ request.form['id'])

    Reseñas.update(request.form)
    return redirect('/dashboard/0')