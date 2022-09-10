from flask_app.config.mysqlconnection import  connectToMySQL

from flask import flash

class Category:
    def __init__(self, data):
        self.name = data['name']
        self.created_at= data['created_at']
        self.updated_at= data['updated_at']
        self.recipes_id = data['recipes_id']

    @staticmethod
    def valida_receta(formulario):
        es_valido =True

        if len(formulario['name']) < 3:
            flash('Debe seleccionar al menos 3 caracteres', 'category')
            es_valido = False

    @classmethod 
    def save(cls, formulario):
        query = "INSERT INTO categorys (name, recipes_id) VALUES (%(name)s, %(recipes_id)s)"
        result = connectToMySQL('my_fridge').query_db(query, formulario)
        return result
        
    