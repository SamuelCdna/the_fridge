from flask_app.config.mysqlconnection import  connectToMySQL

from flask import flash

class Ingrerecipe:
    def __init__(self, data):
        self.ingredient_id = data['ingredient_id']
        self.recipe_id = data['recipe_id']
        self.amount = data['amount']

    
    @classmethod 
    def save(cls, id_recipe,ingredients):
        query = ""
        for i in ingredients:
            query = F" INSERT INTO ingrediente_receta (recipe_id,ingredient_id) VALUES('{id_recipe}','{i}');"
            connectToMySQL('my_fridge').query_db(query)

        
