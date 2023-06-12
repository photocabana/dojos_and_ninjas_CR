
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
# import re
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# The above is used when we do login registration, be sure to install flask-bcrypt: pipenv install flask-bcrypt


class Ninja:
    db = "dojos_and_ninjas" #which database are you using for this project
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojos_id = data['dojos_id']
        # What changes need to be made above for this project?
        #What needs to be added her for class association?



    # Create Users Models

    @classmethod
    def create_ninja(cls, ninja_info):
        query = """
        INSERT INTO ninjas (first_name, last_name, age, dojos_id)
        VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojos_id)s)
        ;"""
        results = connectToMySQL(cls.db).query_db(query, ninja_info)
        return int(results)


    # Read Users Models

    @classmethod
    def get_all_ninjas(cls):
        query = """
        SELECT *
        FROM ninjas
        ;"""
        ninjas_data = connectToMySQL(cls.db).query_db(query)
        ninjas = []
        for ninja in ninjas_data:
            ninjas.append(cls(ninja))
        return ninjas


    # Update Users Models



    # Delete Users Models