from flask import render_template, redirect, session, request, flash
from flask_app import app

#Importación del modelo
from flask_app.models.users import User
from flask_app.models.recipes import Recipes

@app.route('/Creceta')
def Creceta():
    if 'user_id' not in session:
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario)

    return render_template('create_recipe.html', user=user)

@app.route('/create_recipe', methods=['POST'])
def create_recipe():

    if 'user_id' not in session: 
        return redirect('/')

    if not Recipes.valida_receta(request.form): 
        return redirect('/Creceta')

    Recipes.save(request.form)
    return redirect('/dashboard')


    

@app.route('/view/reseña/<int:id>') 
def mostrar_receta(id):
    if 'user_id' not in session:  
        return redirect('/')
    formulario = {
        "id": session['user_id']
    }
    user = User.get_by_id(formulario) 
    formulario_receta = { "id": id }
    recetas = Recipes.get_by_id(formulario_reseña)
    return render_template('mostrar_receta.html', user=user, recetas=recetas)