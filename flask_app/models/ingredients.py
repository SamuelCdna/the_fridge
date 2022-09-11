from flask_app.config.mysqlconnection import  connectToMySQL

from flask import flash

class Ingredient:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at= data['created_at']
        self.updated_at= data['updated_at']

    @staticmethod
    def valida_ingredientes(formulario):
        es_valido =True

        if len(formulario['name']) < 3:
            flash('Debe ingresar al menos 3 caracteres', 'ingrediente')
            es_valido = False

        return es_valido


    @classmethod 
    def save(cls, formulario):
        query = "INSERT INTO ingredients (name) VALUES (%(name)s)"
        result = connectToMySQL('my_fridge').query_db(query, formulario)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ingredients ORDER by name ASC"
        results = connectToMySQL('my_fridge').query_db(query) #Lista de diccionarios 
        ingredientes = []
        for ingrediente in results:
            ingredientes.append(cls(ingrediente)) 
            print(ingredientes)
        return ingredientes

        #PENDIENTES

        #left join acorde con lo que tengan los otros compañeros 

