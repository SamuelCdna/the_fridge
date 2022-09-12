from flask import render_template, redirect, session, request, flash
from flask_app import app

#Importación del modelo
from flask_app.models.users import User
from flask_app.models.recipes import Recipes
from flask_app.models.category import Category 
from flask_app.models.ingredients import Ingredient
from flask_app.controllers import users_controller, recipes_controller, ingredients_controller, category_controller

@app.route('/Creceta')
def Creceta():

    if 'user_id' not in session:
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario)

    categorias= Category.get_all()
    
    return render_template('create_recipe.html', user=user, categorias=categorias)

@app.route('/create_recipe', methods=['POST'])
def create_recipe():
    print('hola')
    print(request.form)

    if 'user_id' not in session: 
        return redirect('/')

    if not Recipes.valida_receta(request.form): 
        return redirect('/Creceta')

    Recipes.save(request.form)
    
    return redirect('/dashboard')

@app.route('/Ccategorys')
def Ccategorys():
    if 'user_id' not in session:
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }
    user = User.get_by_id(formulario)
    return render_template('category.html', user=user)

@app.route('/search-recipes')
def ingredients():
    if 'user_id' not in session:
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }
    return render_template('ingredients.html', user= User.get_by_id(formulario), recipies=[], ingredients = Ingredient.get_all())

@app.route('/view/reseña/<int:id>') 
def mostrar_receta(id):
    if 'user_id' not in session:  
        return redirect('/')
    formulario = {
        "id": session['user_id']
    }
    user = User.get_by_id(formulario) 
    formulario_receta = { "id": id }
    recetas = Recipes.get_by_id(formulario_receta)
    return render_template('mostrar_receta.html', user=user, recetas=recetas)

@app.route('/search_ingredients', methods=['POST'])
def SearchIngredients():
    if 'user_id' not in session: 
        return redirect('/')
    return render_template('ingredients.html', recipes = Recipes.searchRecipiesByIngredients(request.form["search"]), ingredients = Ingredient.get_all())



