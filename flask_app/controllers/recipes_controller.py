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
    
    

    if 'user_id' not in session: 
        return redirect('/')

    if not Recipes.valida_receta(request.form): 
        return redirect('/Creceta')

    Recipes.save(request.form)
    
    return redirect('/dashboard/0')





@app.route('/Ccategorys')
def Ccategorys():
    if 'user_id' not in session:
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario)

    return render_template('category.html', user=user)



@app.route('/view_recipes') 
def view_recipes():
    if 'user_id' not in session:  
        return redirect('/')
    formulario = {
        "id": session['user_id']
    }
    user = User.get_by_id(formulario) 
    recipes = Recipes.get_all()
    return render_template('view_recipesadmi.html', user=user, recipes=recipes)


@app.route('/edit/recipe/<int:id>') 
def edit_receta(id):
    if 'user_id' not in session: 
        return redirect('/')
    formulario = {
        'id': session['user_id']
    }
    
    user = User.get_by_id(formulario) 
    formulario_receta = {"id": id}

    receta = Recipes.get_by_id(formulario_receta)
    categories= Category.get_all()

    return render_template('edit_receta.html', user=user, receta=receta, categories = categories)

@app.route('/update/recipe', methods=['POST'])
def update_reseña():
    if 'user_id' not in session: 
        return redirect('/')

    if not Recipes.valida_receta(request.form): 
        return redirect('/edit/recipe/'+ request.form['id'])

    Recipes.update(request.form)
    return redirect('/view_recipes')

@app.route('/search_recipes', methods=['POST'])
def search_recipes():
    if 'user_id' not in session: 
        return redirect('/')
    return render_template('search_recipes.html', recipes = Recipes.searchRecipiesByIngredients(request.form["search"]), ingredients = Ingredient.get_all())

@app.route('/search_recipes')
def searchRecipes():
    if 'user_id' not in session:
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }
    return render_template('search_recipes.html', user= User.get_by_id(formulario), recipies=[], ingredients = Ingredient.get_all())
    
