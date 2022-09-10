from flask_app.config.mysqlconnection import  connectToMySQL

from flask import flash

class Recipes:
    def __init__(self, data):
        self.name = data['name']
        self.time_cook = data['time_cook']
        self.level_recipe = data['level_recipe']
        self.preference = data['preference']
        self.food_type = data['food_type']
        self.recipescol = data['recipescol']
        self.description = data['description']
        self.preparation = data['preparation']
        self.created_at= data['created_at']
        self.updated_at= data['updated_at']
        self.user_id = data['user_id']
        self.category_id = data['category_id']
    
    @staticmethod
    def valida_receta(formulario):
        es_valido =True

        if len(formulario['name']) < 3:
            flash('el nombre de la receta debe tener al menos 3 caracteres', 'receta')
            es_valido = False
        
        if len(formulario['description']) < 3:
            flash('la descripcion no puede estar vacia ', 'receta')
            es_valido = False
        
        if len(formulario['preparation']) < 3:
            flash('la preparacion no puede estar vacia', 'receta')
            es_valido = False



    @classmethod 
    def save(cls, formulario):
        query = "INSERT INTO recipes (name, time_cook, level_recipe, food_type, description, preparation, user_id ,category_id) VALUES (%(name)s, %(time_cook)s, %(level_recipe)s, %(food_type)s,  %(description)s, %(preparation)s, %(user_id)s , %(category_id)s)"
        result = connectToMySQL('my_fridge').query_db(query, formulario)
        return result
    
    @classmethod
    def get_all(cls):
        query = "SELECT recipes.*, first_name  FROM recipes LEFT JOIN users ON users.id = recipes.user_id;"
        results = connectToMySQL('my_fridge').query_db(query) #Lista de diccionarios 
        recipes = []
        for recipe in results:
            #recipe = diccionario
            recipes.append(cls(recipe)) #1.- cls(recipe) me crea una instancia en base al diccionario, 2.- Agrego la instancia a mi lista de recetas
        return recipes

    @classmethod
    def get_by_id(cls, formulario): #formulario = {id: 1}
        query = "SELECT recipes.*, first_name  FROM recipes LEFT JOIN users ON users.id = recipes.user_id WHERE recipes.id = %(id)s;"
        result = connectToMySQL('my_fridge').query_db(query, formulario) #Lista de diccionarios
        reseña = cls(result[0])
        return reseña

    @classmethod
    def update(cls, formulario):
        query = "UPDATE reseñas SET name=%(name)s, time_cook=%(time_cook)s , level_recipe=%(level_recipe)s , food_type=%(food_type)s , description=%(description)s , preparation=%(preparation)s  WHERE id = %(id)s"
        result = connectToMySQL('my_fridge').query_db(query, formulario)
        return result

    @classmethod
    def delete(cls, formulario): #Recibe formulario con id de receta a borrar
        query = "DELETE FROM recipes WHERE id = %(id)s"
        result = connectToMySQL('my_fridge').query_db(query, formulario)
        return result
