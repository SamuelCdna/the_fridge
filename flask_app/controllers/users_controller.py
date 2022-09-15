from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.controllers import users_controller ,recipes_controller, ingredients_controller,category_controller, reviews_controller

#Importación del modelo
from flask_app.models.users import User
from flask_app.models.recipes import Recipes
from flask_app.models.category import Category 
from flask_app.models.ingredients import Ingredient
#Importación BCrypt
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/registrate', methods=['POST'])
def registrate():
    #Validar la información ingresada
    '''
    if not User.valida_usuario(request.form):
        return redirect('/registro')
    '''
    pwd = bcrypt.generate_password_hash(request.form['password']) #Encriptamos el password del usuario

    formulario = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "level": request.form['level'],
        "level": request.form['level'],
        "permisions": 'user',
        "password": pwd
    }

    #request.form = FORMULARIO HTML
    id = User.save(formulario) #Recibo el identificador de mi nuevo usuario

    session['user_id'] = id

    return redirect('/dashboard/0')

@app.route('/login', methods=['POST'])
def login():

    user = User.get_by_email(request.form) 

    if not user:
        flash('E-mail no encontrado', 'login')
        return redirect('/')

    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Password incorrecto', 'login')
        return redirect('/')

    session['user_id'] = user.id

    return redirect('/dashboard/0')



@app.route('/dashboard/<int:category>')
def dashboarduser(category):

    formulario = {
        'id': session['user_id']
    }
    if 'user_id' not in session:
        return redirect('/')
    
    ingredients = Ingredient.get_all()

    user = User.get_by_id(formulario)
    categories= Category.get_all()

    session['user_id'] = user.id

    if user.id == 1 :
        return render_template('admi_dashboard.html', user=user, )
    else:
        if category == 0:
            recipes= Recipes.get_all()
            return render_template('dashboard.html', user=user, recipes=recipes, categories = categories, ingredients = ingredients)
        else:
            form_category = {
                "id" : category
            }
            
            recipes = Recipes.show_recipes_byid(form_category)

    return render_template('dashboard.html', user=user, recipes=recipes, categories = categories ,ingredients = ingredients)
    
    


# @app.route('/dashboard')#dashboard del administrador
# def dashboard():

#     formulario = {
#         'id': session['user_id']
#     }

#     if 'user_id' not in session:
#         return redirect('/')

#     user = User.get_by_id(formulario)
#     recipes = Recipes.get_all()

#     return render_template('admi_dashboard.html', user=user, recipes=recipes)


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/my_fridge')
def my_fridgee():

    if 'user_id' not in session:
        return redirect('/')
    
    recipes= Recipes.get_all()
    
    ingredients = Ingredient.get_all()
    
    return render_template('search_recipes.html', recipes=recipes ,ingredients = ingredients)
