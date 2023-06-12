
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app.models import ninja
# import re
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# The above is used when we do login registration, be sure to install flask-bcrypt: pipenv install flask-bcrypt


class Dojo:
    db = "dojos_and_ninjas" #which database are you using for this project
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
        # What changes need to be made above for this project?
        #What needs to be added her for class association?



    # Create Users Models

    @classmethod
    def create_dojo(cls, dojo_info):
        query = """
        INSERT INTO dojos (name)
        VALUES (%(name)s)
        ;"""
        results = connectToMySQL(cls.db).query_db(query, dojo_info)
        return int(results)


    # Read Users Models


    @classmethod
    def get_all_dojos(cls):
        query = """
        SELECT *
        FROM dojos
        ;"""
        dojos_data = connectToMySQL(cls.db).query_db(query)
        dojos = []
        for dojo in dojos_data:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def get_dojos_with_ninjas(cls, id):
        data = { 'id' : id }
        query = """
        SELECT *
        FROM dojos
        LEFT JOIN ninjas
        ON ninjas.dojos_id = dojos.id
        WHERE dojos.id = %(id)s
        ;"""
        dojo_data = connectToMySQL(cls.db).query_db(query,data)
        this_dojo = cls(dojo_data[0])
        if dojo_data[0]['first_name']:           
            for row in dojo_data:
                data = {
                    'id' : row['id'],
                    'first_name' : row['first_name'],
                    'last_name' : row['last_name'],
                    'age' : row['age'],
                    'created_at' : row['created_at'],
                    'updated_at' : row['updated_at'],
                    'dojos_id' : row['dojos_id']
                }
                this_dojo.ninjas.append(ninja.Ninja(data))
        return this_dojo


    # Update Users Models



    # Delete Users Models