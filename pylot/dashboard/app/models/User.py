from system.core.model import Model
import re
import bcrypt

class User(Model):
    def __init__(self):
        super(User, self).__init__()


    # def get_users(self):
        # query = "select * from users order by updated_at desc"
        # values = {}
        # users = self.db.query_db(query, values)
        # return {
                # 'status': True,
                # 'users': users
                # }


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
                'description': description
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
        result = {
                'status': status,
                'user': user[0]
                }
        return result


    def get_all_users(self):
        query = "select id, email, first_name, last_name, user_level, description, created_at from users order by id asc"
        values = {}
        users = self.db.query_db(query, values)
        return {
                'status': True,
                'users': users
                }


###########

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

