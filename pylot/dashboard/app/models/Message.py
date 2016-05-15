"""
    Sample Model File

    A Model should be in charge of communicating with the Database.
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
import re

class Message(Model):
    def __init__(self):
        super(Message, self).__init__()


    def get_messages(self):
        query = "select * from messages order by updated_at desc"
        values = {}
        messages = self.db.query_db(query, values)
        return {
                'status': True,
                'messages': messages
                }


    def create_message(self, req):
        number_pattern = r"^\d+$"
        if not re.match(number_pattern, req['price']):
            return {
                    'status': False,
                    'messages': ["Price must be number"]
                    }
        query = "insert into messages (name, description, price, created_at, updated_at) values (:name, :description, :price, NOW(), NOW())"
        values = {
                'name': req['name'],
                'description': req['description'],
                'price': req['price']
                }
        message = self.db.query_db(query, values)
        result = {
                'status': True,
                'message': message
                }
        return result

    def get_message(self, id):
        query = "select * from messages where id = :id limit 1"
        values = {
                'id': id
                }
        message = self.db.query_db(query, values)
        result = {
                'status': True,
                'message': message[0]
                }
        return result

    def update_message(self, id, req):
        number_pattern = r"^\d+$"
        if not re.match(number_pattern, req['price']):
            return {
                    'status': False,
                    'messages': ["Price must be number"]
                    }
        query = "update messages set name=:name, description = :description, price = :price, updated_at = NOW() where id = :id"
        values = {
                'id': id,
                'name': req['name'],
                'description': req['description'],
                'price': req['price']
                }
        message = self.db.query_db(query, values)
        result = {
                'status': True,
                'message': message
                }
        return message

    def destroy_message(self, req):
        query = "delete from messages where id = :id"
        values = {
                'id': req['id']
                }
        message = self.db.query_db(query, values)
        result = {
                'status': True,
                'message': message
                }
        return message

