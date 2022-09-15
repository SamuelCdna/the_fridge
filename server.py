#EJECUTA nuestra aplicación
from flask_app import app

#Importando mi controlador
from flask_app.controllers import users_controller ,recipes_controller , ingredients_controller, category_controller,reviews_controller

if __name__=="__main__":
    app.run(debug=True)