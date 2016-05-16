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


    def get_messages(self, target_user_id):
        query = "select messages.*, authors.id as author_id, authors.first_name as author_first_name, authors.last_name as author_last_name from messages inner join users as authors on messages.author_id = authors.id where messages.user_id = :user_id order by messages.updated_at desc"
        values = {
                'user_id': target_user_id
                }
        messages = self.db.query_db(query, values)
        return {
                'status': True,
                'messages': messages
                }


    def create(self, req, author_user_id):
        print 'model message create start'
        # query = "select * from messages where user_id = :user_id order by updated_at desc"
        query = "insert into messages (user_id, author_id, message, created_at, updated_at) values (:target_user_id, :author_id, :message, NOW(), NOW())"
        values = {
                'target_user_id': req['target_user_id'],
                'author_id': author_user_id,
                'message': req['message']
                }
        result = self.db.query_db(query, values)
        print 'result===', result

        return {
                'status': True,
                'messages': result
                }

