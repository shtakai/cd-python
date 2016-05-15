"""
    Sample Model File

    A Model should be in charge of communicating with the Database.
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
import re

class User(Model):
    def __init__(self):
        super(User, self).__init__()


    def get_users(self):
        query = "select * from users order by updated_at desc"
        values = {}
        users = self.db.query_db(query, values)
        return {
                'status': True,
                'users': users
                }


    def create_user(self, req):
        number_pattern = r"^\d+$"
        if not re.match(number_pattern, req['price']):
            return {
                    'status': False,
                    'messages': ["Price must be number"]
                    }
        query = "insert into users (name, description, price, created_at, updated_at) values (:name, :description, :price, NOW(), NOW())"
        values = {
                'name': req['name'],
                'description': req['description'],
                'price': req['price']
                }
        user = self.db.query_db(query, values)
        result = {
                'status': True,
                'user': user
                }
        return result

    def get_user(self, id):
        query = "select * from users where id = :id limit 1"
        values = {
                'id': id
                }
        user = self.db.query_db(query, values)
        result = {
                'status': True,
                'user': user[0]
                }
        return result

    def update_user(self, id, req):
        number_pattern = r"^\d+$"
        if not re.match(number_pattern, req['price']):
            return {
                    'status': False,
                    'messages': ["Price must be number"]
                    }
        query = "update users set name=:name, description = :description, price = :price, updated_at = NOW() where id = :id"
        values = {
                'id': id,
                'name': req['name'],
                'description': req['description'],
                'price': req['price']
                }
        user = self.db.query_db(query, values)
        result = {
                'status': True,
                'user': user
                }
        return user

    def destroy_user(self, req):
        query = "delete from users where id = :id"
        values = {
                'id': req['id']
                }
        user = self.db.query_db(query, values)
        result = {
                'status': True,
                'user': user
                }
        return user

