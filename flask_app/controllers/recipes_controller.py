from flask import render_template, redirect, session, request, flash, jsonify
from flask_app import app

#Importación del modelo
from flask_app.models.users import User
from flask_app.models.recipes import Recipes
from flask_app.models.category import Category 
from flask_app.models.ingredients import Ingredient
from flask_app.models.ingredient_receta import Ingrerecipe
from flask_app.models.reviews import Reseñas
from flask_app.controllers import users_controller, recipes_controller, ingredients_controller, category_controller, reviews_controller

@app.route('/Creceta')
def Creceta():

    if 'user_id' not in session:
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario)

    ingredients = Ingredient.get_all()

    categorias= Category.get_all()
    
    return render_template('create_recipe.html', user=user, categorias=categorias, ingredients= ingredients)


    

@app.route('/create_recipe', methods=['POST'])
def create_recipe():
    
    

    if 'user_id' not in session: 
        return redirect('/')

    if not Recipes.valida_receta(request.form): 
        return redirect('/Creceta')


    id_recipe = Recipes.save(request.form)
    
    Ingrerecipe.save(id_recipe,request.form.getlist('ingredients[]'))

    
    return jsonify(message="correcto")





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
    recipes = Recipes.recipe_and_category()
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

    receta = Recipes.recipe_and_category_by_id_recipe(formulario_receta)
    
    categories= Category.get_all()
    return render_template('edit_receta.html', user=user, receta=receta, categories = categories)


@app.route('/update/recipe', methods=['POST'])
def update_receta():
    if 'user_id' not in session: 
        return redirect('/')

    if not Recipes.valida_receta(request.form): 
        return redirect('/edit/recipe/'+ request.form['id'])

    Recipes.update(request.form)
    return redirect('/view_recipes')


@app.route('/delete/<int:id>')
def delete_receta(id):
    if 'user_id' not in session: 
        return redirect('/')
    
    formulario = {"id": id}
    Ingrerecipe.delete(formulario)
    Recipes.delete(formulario)
    return redirect('/view_recipes')


@app.route('/search_recipes', methods=['POST'])
def search_recipes():
    if 'user_id' not in session: 
        return redirect('/')
    search_list = request.form.getlist('search[]')    
    if len(search_list)<=0:
        print('No seleccionó nada')
        return redirect('/searchRecipes')
    else:
        return render_template('search_recipes.html', recipes = Recipes.searchRecipiesByIngredients(search_list), ingredients = Ingredient.get_all())

@app.route('/searchRecipes')
def searchRecipes():
    if 'user_id' not in session:
        return redirect('/')
    

    formulario = {
        'id': session['user_id']
    }
    return render_template('search_recipes.html', user= User.get_by_id(formulario), recipies=[], ingredients = Ingredient.get_all())
    

@app.route('/view_receta/<int:id>') 
def view_recetas(id):
    if 'user_id' not in session:  
        return redirect('/')
    formulario = {
        "id": session['user_id']
    }
    user = User.get_by_id(formulario) 
    formulario_receta = {"id": id}
    receta = Recipes.prueba(formulario_receta)
    reseñas = Reseñas.get_reseñas()
    # print(receta['ingrediente'])
    return render_template('view_recipe.html', user=user, recipe=receta, reseñas=reseñas)