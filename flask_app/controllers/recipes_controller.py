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

# @app.route('/ingredients')
# def ingredients():
#     if 'user_id' not in session:
#         return redirect('/')

#     formulario = {
#         'id': session['user_id']
#     }

#     user = User.get_by_id(formulario)

#     return render_template('ingredients.html', user=user, recipies=[])

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
    categorias= Category.get_all()

    return render_template('edit_receta.html', user=user, receta=receta, categorias=categorias)

@app.route('/update/recipe', methods=['POST'])
def update_reseña():
    if 'user_id' not in session: 
        return redirect('/')

    if not Recipes.valida_receta(request.form): 
        return redirect('/edit/recipe/'+ request.form['id'])

    Recipes.update(request.form)
    return redirect('/view_recipes')



# @app.route('/edit/recipe')
# def edit_reci():

    if 'user_id' not in session:  
        return redirect('/')

    formulario = {
        "id": session['user_id']
    }

    id = id_recipe

    user = User.get_by_id(formulario) 
    categorias= Category.get_all()
    recipe = Recipes.get_by_id(id)

    return render_template('all_recipes.html', user=user, recipe=recipe, categorias=categorias)

@app.route('/search_ingredients1', methods=['POST'])
def SearchIngredients1():
    if 'user_id' not in session: 
        return redirect('/')
    return render_template('ingredients.html', recipes = Recipes.searchRecipiesByIngredients(request.form["search"]), ingredients = Ingredient.get_all())


@app.route('/search_ingredients', methods=['POST'])
def SearchIngredients():
    if 'user_id' not in session: 
        return redirect('/')
    return render_template('ingredients.html', recipes = Recipes.searchRecipiesByIngredients(request.form["search"]), ingredients = Ingredient.get_all())
