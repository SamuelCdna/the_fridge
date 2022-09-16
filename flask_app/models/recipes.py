from flask_app.config.mysqlconnection import  connectToMySQL

from flask import flash

class Recipes:
    def __init__(self, data):
        self.name = data['name']
        self.time_cook = data['time_cook']
        self.level_recipe = data['level_recipe']
        self.id = data['id']
        self.description = data['description']
        self.preparation = data['preparation']
        self.created_at= data['created_at']
        self.updated_at= data['updated_at']
        self.user_id = data['user_id']
        self.category_id = data['category_id']
        self.img = data['img']

        if 'categoria' in data :
            self.categoria = data['categoria']
        
    
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
        
        return es_valido



    @classmethod 
    def save(cls, formulario):
        query = "INSERT INTO recipes (name, time_cook, level_recipe, description, preparation, user_id, category_id , img ) VALUES (%(name)s, %(time_cook)s, %(level_recipe)s,  %(description)s, %(preparation)s, %(user_id)s ,%(category_id)s,%(img)s)"
        result = connectToMySQL('my_fridge').query_db(query, formulario)
        print(result)
        return result
    
    @classmethod
    def get_all(cls):#"SELECT recipes.*, first_name  FROM recipes LEFT JOIN users ON users.id = recipes.user_id;"
        query = "SELECT * FROM recipes;"
        results = connectToMySQL('my_fridge').query_db(query) #Lista de diccionarios 
        recipes = []
        for recipe in results:
            recipes.append(cls(recipe)) #1.- cls(recipe) me crea una instancia en base al diccionario, 2.- Agrego la instancia a mi lista de recetas
        return recipes

    @classmethod
    def recipe_and_category(cls): 
        query = "SELECT *, categorys.name AS categoria FROM recipes LEFT JOIN categorys ON recipes.category_id = categorys.id ;"
        results = connectToMySQL('my_fridge').query_db(query) 
        recipescategory = []
        for recipe in results:
            recipescategory.append(cls(recipe))
        return recipescategory

    @classmethod
    def get_by_id(cls, formulario): #formulario = {id: 1}
        query = "SELECT recipes.*, first_name  FROM recipes LEFT JOIN users ON users.id = recipes.user_id WHERE recipes.id = %(id)s;"
        result = connectToMySQL('my_fridge').query_db(query, formulario) #Lista de diccionarios
        reseña = cls(result[0])
        return reseña

    @classmethod
    def update(cls, formulario):
        query = "UPDATE recipes SET name=%(name)s, time_cook=%(time_cook)s , level_recipe=%(level_recipe)s , description=%(description)s , preparation=%(preparation)s, img=%(img)s WHERE id = %(id)s"
        result = connectToMySQL('my_fridge').query_db(query, formulario)
        return result

    def delete(cls, formulario): #Recibe formulario con id de receta a borrar
        query = "DELETE FROM ingrediente_receta WHERE recipe_id = %(id)s"
        result = connectToMySQL('my_fridge').query_db(query, formulario)
        return result

    @classmethod
    def searchRecipiesByIngredients(cls, filter):
        condition = ""
        for item in filter:
            if condition == "":
                condition = F"I.name like '%{item}%'"
            else:
                condition += F" or I.name like '%{item}%'"
        query = F"SELECT DISTINCT R.* FROM  my_fridge.recipes R inner join my_fridge.ingrediente_receta IR on(R.id=IR.recipe_id) inner join my_fridge.ingredients I on(I.id = IR.ingredient_id) where {condition}"
        result = connectToMySQL('my_fridge').query_db(query)
        recipes = []
        for recipe in result:
            #recipe = diccionario
            recipes.append(cls(recipe))
        return recipes


    @classmethod
    def show_recipes_byid(cls, formulario):
        print(formulario)
        query = "SELECT * FROM recipes WHERE category_id = %(id)s"
        result = connectToMySQL('my_fridge').query_db(query, formulario)
        recipes = []
        for recipe in result:
            recipes.append(cls(recipe))
        return recipes

    # @classmethod
    # def categoria_id(cls, formulario):
    #     query = "SELECT * FROM recipes WHERE category_id = %(category_id)s"
    #     result = connectToMySQL('my_fridge').query_db(query, formulario)
    #     print(result)
    #     recipe = cls(result[0]) #creamos una instancia de recipes
    #     return recipe

    @classmethod
    def prueba(cls,formulario):
        query = "SELECT * FROM recipes WHERE id = %(id)s"
        result = connectToMySQL('my_fridge').query_db(query,formulario) 
        recipe = cls(result[0])             
        for recipe in result:
            query = "SELECT name, amount, icon FROM ingrediente_receta INNER JOIN ingredients ON ingredient_id = ingredients.id WHERE recipe_id = "+str(recipe['id'])
            result_receta = connectToMySQL('my_fridge').query_db(query)
            ingredients = []
            for ingredient in result_receta:
                ingredients.append(ingredient)

            recipe['ingrediente'] = ingredients
            # print('aqui es un nueva receta')
            # print(recipe['ingrediente'])
        return recipe
