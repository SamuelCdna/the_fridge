from flask_app.config.mysqlconnection import  connectToMySQL

from flask import flash

class Category:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.icon = data['icon']
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
        query = "SELECT * FROM my_fridge.categorys ORDER by name ASC;"
        results = connectToMySQL('my_fridge').query_db(query) #Lista de diccionarios 
        categorias = []
        for categoria in results:
            
            categorias.append(cls(categoria)) 
        
        return categorias



        
    @classmethod
    def get_by_id(cls, formulario): 
        query = "SELECT * FROM categorys WHERE id = %(id)s;"
        result = connectToMySQL('my_fridge').query_db(query, formulario) #Lista de diccionarios
        category = cls(result[0])
        print(category)
        return category


    @classmethod
    def update(cls, formulario):
        query = "UPDATE categorys SET name=%(name)s WHERE id = %(id)s"
        connectToMySQL('my_fridge').query_db(query, formulario)


    @classmethod
    def delete(cls, formulario):
        query = "DELETE FROM categorys WHERE id = %(id)s"
        connectToMySQL('my_fridge').query_db(query,formulario)