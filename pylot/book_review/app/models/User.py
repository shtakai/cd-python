from system.core.model import Model
import re
import bcrypt

class User(Model):
    def __init__(self):
        super(User, self).__init__()

    def register(self, req):
        errors = []
        email_pattern = r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$'
        # guard for empty
        for k, v in req.items():
            if len(v) == 0:
                errors.append("{} can not be empty".format(k))
        if errors:
            return {
                    'status': False,
                    'errors': errors
                    }

        if not re.match(email_pattern, req['email']):
            errors.append("email is invalid")
        if len(req['name']) < 4:
            errors.append("name should contain at least 4 letters")
        if len(req['alias']) < 4:
            errors.append("alias should contain at least 4 letters")
        if len(req['password']) < 8:
            errors.append("password should contain at least 8 letters")
        if req['password'] != req['confirm_password']:
            errors.append("password and password confirmation aren't matched")
        if errors:
            return {
                    'status': False,
                    'errors': errors
                    }

        # email double checking
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

        query = "insert into users (email, name, alias, pw_hash, created_at, updated_at) values (:email, :name, :alias, :pw_hash, NOW(), NOW())"
        values = {
                'email': req['email'],
                'name': req['name'],
                'alias': req['alias'],
                'pw_hash': self.bcrypt.generate_password_hash(req['password'])
                }
        user = self.db.query_db(query, values)
        result = {
                'status': True,
                'user': user
                }
        return result

    def login(self, req):
        errors = []
        query = "select * from users where email = :email limit 1"
        values = {
                'email': req['email']
                }
        result = self.db.query_db(query, values)
        if not result:
            errors.append('login failed')
            return {
                    'status': False,
                    'errors': errors
                    }

        user = result[0]
        if not self.bcrypt.check_password_hash(user['pw_hash'], req['password']):
            errors.append('login failed')
            return {
                    'status': False,
                    'errors': errors
                    }

        del(user['pw_hash'])
        return {
                'status': True,
                'user': user,
                'user_id': user['id'],
                'user_name': user['name'],
                'user_alias': user['alias'],
                'user_email': user['email']
                }

    def get_user(self, user_id):
        # query = 'select id, name, alias, email, created_at, updated_at from users where id = :id'
        # get user information with review count
        query = 'select users.id, users.name, users.alias, users.email, users.created_at, users.updated_at, count(*) as review_count from users inner join reviews on users.id = reviews.user_id where users.id = :user_id group by users.id limit 1'
        values = {
                'user_id': user_id
                }
        user_result = self.db.query_db(query, values)
        # get book titles reviewed by this user
        query = 'select distinct books.id, books.title from books inner join reviews on books.id = reviews.book_id inner join users on reviews.user_id = users.id where users.id = :user_id order by reviews.updated_at desc'
        values = {
                'user_id': user_id
                }
        book_result = self.db.query_db(query, values)
        return {
                'status': True,
                'user': user_result[0],
                'reviewed_books': book_result
                }

