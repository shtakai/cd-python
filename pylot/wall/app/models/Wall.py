"""
    Sample Model File

    A Model should be in charge of communicating with the Database.
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
import re

class Wall(Model):
    def __init__(self):
        super(Wall, self).__init__()

    def login(self, req):
        query = 'select * from users where email = :email limit 1'
        value = {
                'email': req['email'],
                }
        try:
            tmp_user = self.db.query_db(query, value)
            if self.bcrypt.check_password_hash(tmp_user[0]['pw_hash'], req['password']):
                return {
                    'status': True,
                    'user_id': tmp_user[0]['id'],
                    'user' : tmp_user[0]['first_name'] + ' ' + tmp_user[0]['last_name']
                }
            else:
                return { 'status': False }
        except:
            return {'status': False}

    def register(self, req):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        messages = []
        for k, v in req.items():
            if len(v) == 0:
                messages.append("{} is mandatory".format(k))
        # check vaidation and return error ASAP if validation failed
        if not EMAIL_REGEX.match(req['email']):
            messages.append('email address is not correct form')
        if req['password'] != req['confirm_password']:
            messages.append('password and password confirmation not match')
        if len(req['first_name']) > 2:
            messages.append('first name must be 2 letters at least')
        if len(req['last_name']) > 2:
            messages.append('last name must be 2 letters at least')
        if len(req['password']) > 8:
            messages.append('password must be 8 letters at least')

        if len(messages) > 0:
            return {
                'status': False,
                'message': messages
            }
        query = "insert into users (first_name, last_name, email, pw_hash,  created_at, updated_at) values (:first_name, :last_name, :email, :password, NOW(),NOW())"
        values = {
                'first_name': req['first_name'],
                'last_name': req['last_name'],
                'email': req['email'],
                'password': self.bcrypt.generate_password_hash(req['password'])
                }
        user = self.db.query_db(query, values)
        try:
            return {
                'status': True,
                'user': user,
                'message': ['created user successful']
            }
        except:
            return {
                'status': False,
                'message': ['create failed']
            }
        return {
            'status': False,
            'message': ['create failed']
        }

    def get_messages(self):
        messages = []
        query = "select messages.*, users.first_name, users.last_name from messages inner join users on messages.user_id = users.id order by id desc"
        values = {}
        result = self.db.query_db(query, values)

        for m in result:
            query = "select comments.*, users.first_name, users.last_name from comments inner join users on comments.user_id = users.id where comments.message_id = :message_id order by comments.id desc"
            values = {
                    'message_id': m['id']
                    }
            comments = self.db.query_db(query, values)
            messages.append({
                'message': m,
                'comments': comments
                })

        return {
            'status': True,
            'messages': messages
            }

    def post_message(self, req, user_id):
        query = "insert into messages (message, user_id, created_at, updated_at) values (:message, :user_id, NOW(), NOW())"
        values = {
                'message' : req['message'],
                'user_id' : user_id
                }
        result = self.db.query_db(query, values)

        return {
            'status': True,
            'result': result
            }

    def post_comment(self, req, user_id):
        query = "insert into comments (comment, user_id, message_id, created_at, updated_at) values (:comment, :user_id, :message_id, NOW(), NOW())"
        values = {
                'comment' : req['comment'],
                'user_id' : user_id,
                'message_id': req['message_id']
                }
        result = self.db.query_db(query, values)

        return {
            'status': True,
            'result': result
            }


