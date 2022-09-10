from flask_app.config.mysqlconnection import  connectToMySQL

from flask import flash

class Category:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at= data['created_at']
        self.updated_at= data['updated_at']
        

    @staticmethod
    def valida_categoria(formulario):
        es_valido =True

        if len(formulario['name']) < 3:
            flash('Debe seleccionar al menos 3 caracteres', 'categoria')
            es_valido = False

        return es_valido

    @classmethod 
    def save(cls, formulario):
        query = "INSERT INTO categorys (name) VALUES (%(name)s)"
        result = connectToMySQL('my_fridge').query_db(query, formulario)
        return result
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM categorys;"
        results = connectToMySQL('my_fridge').query_db(query) #Lista de diccionarios 
        categorias = []
        for categoria in results:
            #recipe = diccionario
            categorias.append(cls(categoria)) 
            print(categoria)#1.- cls(recipe) me crea una instancia en base al diccionario, 2.- Agrego la instancia a mi lista de recetas
        return categorias