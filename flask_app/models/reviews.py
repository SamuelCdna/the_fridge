from flask_app.config.mysqlconnection import  connectToMySQL

from flask import flash

class Reseñas:
    def __init__(self, data):
        self.id = data['id']
        self.contenido = data['contenido']
        self.rate = data['rate']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.recipe_id = data['recipe_id']
        

    @staticmethod
    def valida_reseña(formulario):
        es_valido =True

        if len(formulario['contenido']) < 1:
            flash('La reseña no puede estar vacia', 'reseña')
            es_valido = False

        return es_valido

    @classmethod 
    def save(cls, formulario):
        query = "INSERT INTO reviews (contenido, rate, user_id, recipe_id) VALUES (%(contenido)s, %(rate)s, %(user_id)s, %(recipe_id)s)"
        result = connectToMySQL('my_fridge').query_db(query, formulario)
        return result

    @classmethod 
    def get_reseñas(cls):
        query = "SELECT reviews.*, first_name FROM reviews LEFT JOIN users ON users.id = reviews.user_id;"
        results = connectToMySQL('my_fridge').query_db(query)
        reseñas = []
        for reseña in results:
            reseñas.append(cls(reseña))
            print(reseña)
        return reseñas

    @classmethod
    def get_by_id(cls, formulario): #formulario = {id: 1}
        query = "SELECT reviews.*, first_name  FROM reviews LEFT JOIN users ON users.id = reviews.user_id WHERE reviews.id = %(id)s;"
        result = connectToMySQL('my_fridge').query_db(query, formulario) #Lista de diccionarios
        reseña = cls(result[0])
        return reseña

    @classmethod
    def update(cls, formulario):
        query = "UPDATE reviews SET contenido=%(contenido)s, rate=%(rate)s WHERE id = %(id)s"
        result = connectToMySQL('my_fridge').query_db(query, formulario)
        return result


    @classmethod
    def delete(cls, formulario): #Recibe formulario con id de receta a borrar
        query = "DELETE FROM reviews WHERE id = %(id)s"
        result = connectToMySQL('my_fridge').query_db(query, formulario)
        return result

