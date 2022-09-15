from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.controllers import users_controller ,recipes_controller, category_controller, ingredients_controller, reviews_controller
from flask_app.models.users import User
from flask_app.models.recipes import Recipes
from flask_app.models.category import Category
from flask_app.models.ingredients import Ingredient

@app.route('/create/category')
def createcategory():

    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/')
        
    return render_template('save_category.html')

@app.route('/save_category', methods=['POST'])
def save_category():
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/')

    if not Category.valida_categoria(request.form): #llama a la función de valida_receta enviándole el formulario, comprueba que sea valido 
        return redirect('/create/category')

    Category.save(request.form)

    return redirect('/view/category')


@app.route('/view/category')
def view_category():
    if 'user_id' not in session: 
        return redirect('/')

    categories = Category.get_all()

    return render_template('view_category.html', categories = categories)

@app.route('/edit_categories/<int:id>') #a través de la URL recibimos el ID de la receta
def edit_categories(id):
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/')
    formulario = { 
        'id': session['user_id']
        }
    user = User.get_by_id(formulario)   

    formulario_categories = {"id": id}

    categoria = Category.get_by_id(formulario_categories)    
    
    
    return render_template('edit_category.html', user=user, categoria=categoria )


@app.route('/update_categories', methods=['POST'])
def update_categories():

    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/') #revisar aqui
    
    

    if not Category.valida_categoria(request.form): 
        return redirect('/edit_categories/'+ request.form['categoria.id'])

    Category.update(request.form)

    return redirect('/view/category')

@app.route('/delete_categories/<int:id>') #a través de la URL recibimos el ID de la receta
def delete_categories(id):
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/')
    formulario_categories = {"id": id}

    Category.delete(formulario_categories) 
    return redirect ('/view/category')