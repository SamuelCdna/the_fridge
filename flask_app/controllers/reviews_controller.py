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

@app.route('/delete/reseña/<int:id>/<int:id_re>')
def delete_reseña(id,id_re):
    if 'user_id' not in session: 
        return redirect('/')
    id_recipe = id_re
    formulario = {"id": id}
    Reseñas.delete(formulario)
    return redirect('/view_receta/'+str(id_recipe))

@app.route('/edit/reseña/<int:id>/<int:id_re>') 
def edit_reseña(id,id_re):
    if 'user_id' not in session: 
        return redirect('/')
    formulario = {
        'id': session['user_id']
    }
    user = User.get_by_id(formulario) 
    formulario_reseña = {"id": id}
    form_recipe = {"id":id_re}
    reseña = Reseñas.get_by_id(formulario_reseña)
    recipe = Recipes.recipe_and_category_by_id_recipe(form_recipe)
    return render_template('edit_reseña.html', user=user, reseña=reseña, recipe=recipe)

@app.route('/update/reseña', methods=['POST'])
def update_res():
    print(request.form['id'])
    if 'user_id' not in session: 
        return redirect('/')

    if not Reseñas.valida_reseña(request.form): 
        return redirect('/edit/reseña/'+ request.form['id'])
    print("....el id es")
    print(request.form['id_recipe'])
    
    Reseñas.update(request.form)
    return redirect('/view_receta/'+ request.form['id_recipe'])