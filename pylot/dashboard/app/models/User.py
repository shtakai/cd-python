from system.core.model import Model
import re
import bcrypt

class User(Model):
    def __init__(self):
        super(User, self).__init__()



    def register(self, req):
        errors = []
        email_pattern = r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$'
        if not re.match(email_pattern, req['email']):
            errors.append("email is invalid")
        if len(req['first_name']) < 2:
            errors.append("first name should contain at least 3 letters")
        if len(req['last_name']) < 2:
            errors.append("last name should contain at least 3 letters")
        if len(req['password']) < 8:
            errors.append("password should contail at least 8 letters")
        for k, v in req.items():
            if len(v) == 0:
                errors.append("{} is mandatory".format(k))
        if req['password'] != req['password_confirmation']:
            errors.append("password and password confirmation aren't matched")
        query = "select id from users where email = :email limit 1"
        values = {
                'email': req['email']
                }
        dup_user = self.db.query_db(query, values)
        if dup_user:
            errors.append("this email address is already used")

        if errors:
            return{
                    'status': False,
                    'errors': errors
                    }

        query = "select count(*) as number_of_users from users"
        values = {}
        number_of_users = self.db.query_db(query, values)
        print 'number_of_users', number_of_users[0]['number_of_users']
        user_level = 9 if number_of_users[0]['number_of_users'] == 0 else 1

        query = "insert into users (email, first_name, last_name, pw_hash, user_level, description, created_at, updated_at) values (:email, :first_name, :last_name, :pw_hash, :user_level, :description, NOW(), NOW())"
        values = {
                'email': req['email'],
                'first_name': req['first_name'],
                'last_name': req['last_name'],
                'pw_hash': self.bcrypt.generate_password_hash(req['password']),
                'user_level': user_level,
                'description': req['description']
                }
        user = self.db.query_db(query, values)

        result = {
                'status': True,
                'user': user
                }
        return result


    def login(self, req):
        query = "select * from users where email = :email"
        values = {
                'email': req['email']
                }
        users = self.db.query_db(query, values)
        if not users:
            return{
                    'status': False,
                    'errors': ['login failed']
                    }

        if not self.bcrypt.check_password_hash(users[0]['pw_hash'], req['password']):
            return{
                    'status': False,
                    'errors': ['login failed']
                    }

        user = users[0]
        return {
                'status': True,
                'user': user['id'],
                'user_name': user['first_name'] + ' ' + user['last_name'],
                'user_level': user['user_level']
                }


    def get_user_info(self, id):
        query = "select id, first_name, last_name, email, user_level, description from users where id = :id limit 1"
        values = {
                'id': id
                }
        result = self.db.query_db(query, values)
        if not result:
            return {
                    'status': False,
                    'errors': ["cannnot get user id:{}".format(id)]
                    }

        user = result[0]
        return {
                'status': True,
                'user': user['id'],
                'user_name':  user['first_name'] + ' ' + user['last_name'],
                'user_level': user['user_level'],
                'user_description': user['description']
                }


    def get_user(self, id):
        query = "select * from users where id = :id limit 1"
        values = {
                'id': id
                }
        user = self.db.query_db(query, values)
        status = True if user[0] else False
        del(user[0]['pw_hash'])
        result = {
                'status': status,
                'user': user[0]
                }
        return result


    def get_all_users(self):
        query = "select id, email, first_name, last_name, user_level, description, created_at from users order by updated_at desc"
        values = {}
        users = self.db.query_db(query, values)
        return {
                'status': True,
                'users': users
                }

    def update_user_admin(self, req):
        errors = []
        email_pattern = r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$'
        if not re.match(email_pattern, req['email']):
            errors.append("email is invalid")
        if len(req['first_name']) < 2:
            errors.append("first name should contain at least 3 letters")
        if len(req['last_name']) < 2:
            errors.append("last name should contain at least 3 letters")
        # WIP does not work
        # print '***** user_level', req['user_level']
        # if not (req['user_level'] == 1 or req['user_level'] == 9):
            # errors.append("user level is 1 or 9")
        for k, v in req.items():
            if len(v) == 0:
                errors.append("{} is mandatory".format(k))
        query = "select id from users where email = :email and id != :id limit 1"
        values = {
                'email': req['email'],
                'id': req['id']
                }
        dup_user = self.db.query_db(query, values)
        print 'DUP user', dup_user
        if dup_user:
            errors.append("this email address is already used")

        if errors:
            return{
                    'status': False,
                    'errors': errors
                    }

        query = "update users set email = :email, first_name = :first_name, last_name = :last_name, description = :description, user_level = :user_level, updated_at = NOW() where id = :id"
        values = {
                'id': req['id'],
                'email': req['email'],
                'first_name': req['first_name'],
                'last_name': req['last_name'],
                'description': req['description'],
                'user_level': req['user_level'],
                'description': ''
                }
        result = self.db.query_db(query, values)
        print 'result--', result
        return {
                'status': True,
                'user': result
                }


    def update_user_password_admin(self, req):
        errors = []
        user = self.get_user(req['id'])
        print '====user', user
        print '====user', user['user']
        if len(req['password']) < 8:
            errors.append('password must be more than 8 letters')
        if req['password'] != req['password_confirmation']:
            errors.append('password and password_confirmation are not matched')
        if errors:
            return {
                    'status': False,
                    'errors': errors,
                    'user': user['user']
                    }
        query = "update users set pw_hash = :pw_hash, updated_at = NOW() where id = :id"
        values = {
                'pw_hash': self.bcrypt.generate_password_hash(req['password']),
                'id': req['id']
                }
        result = self.db.query_db(query, values)

        return{
                'status': True,
                'user': user['user']
                }

    def destroy(self, req):
        errors = []
        query = "delete from users where id = :id"
        values = {
                'id' : req['id']
                }
        result = self.db.query_db(query, values)
        print '---result', result
        return {
                'status': True
                }


    def create(self, req):
        print 'create-----', req
        result = self.register(req)
        print '---result',result
        return result




