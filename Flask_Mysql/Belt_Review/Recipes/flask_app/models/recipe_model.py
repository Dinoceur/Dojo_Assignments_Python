from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.time = data['time']
        self.user_id = data['user_id']
        

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO recipes (user_id, name, description, instructions, time) VALUES (%(user_id)s, %(name)s,%(description)s,%(instructions)s,%(time)s);'
        result = connectToMySQL('recipes').query_db(query,data)
        return result

    @classmethod
    def update(cls,data):
        query = 'UPDATE recipes SET name=%(name)s,description=%(description)s,instructions=%(instructions)s,updated_at=NOW() WHERE id = %(id)s;'
        return connectToMySQL('recipes').query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        result = connectToMySQL('recipes').query_db(query,data)
        return result

    @classmethod
    def get_one(cls,**data):
        query = 'SELECT * FROM recipes WHERE id = %(id)s;' 
        result = connectToMySQL('recipes').query_db(query,data)
        if result:
            return cls(result[0])

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL('recipes').query_db(query)
        recipes = []
        for u in results:
            recipes.append( cls(u) )
        return recipes

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe['name']) < 3:
            flash('Name must be at least 3 characters.','Recipe')
            is_valid = False
        if len(recipe['description']) < 3:
            flash('Description must be at least 3 characters.','Recipe')
            is_valid = False
        if len(recipe['instructions']) < 3:
            flash('Instructions must be at least 3 characters.','Recipe')
            is_valid = False
        return is_valid 