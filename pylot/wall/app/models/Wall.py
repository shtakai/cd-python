"""
    Sample Model File

    A Model should be in charge of communicating with the Database.
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Wall(Model):
    def __init__(self):
        super(Wall, self).__init__()


    def get_all_users(self):
        print self.db.query_db("select * from users")

    def login(self, req):
        print 'login'
        query = 'select * from users where email = ":email" limit 1'
        value = {
                'email': req['email'],
                }
        try:
            tmp_user = self.db.query_db(query, value)
            if self.bcrypt.check_password_hash(tmp_user[0]['pw_hash'], req['password']):
                return (tmp_user[0]['id'], tmp_user[0]['first_name'] + ' ' + tmp_user[0]['last_name'])
            else:
                return False
        except:
            return False

    def register(self, req):
        messages = []
        for k, v in req.items():
            if len(v) == 0:
                messages.append(k,"is mandatory")

        # print self.db.query_db("select * from users")

        query = "insert into users (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (':first name', ':last name', ':email', ':password', NOW(),NOW())"
        # query = 'insert into users (first_name, last_name, email, pw_hash,  created_at, updated_at) values (":first_name", ":last_name", ":email", ":password", NOW(),NOW())'
        values = {
                'first_name': req['first_name'],
                'last_name': req['last_name'],
                'email': req['email'],
                'password': self.bcrypt.generate_password_hash(req['password'])
                }
        print "query", query
        print "value", values

        user = self.db.query_db(query, values)
        print "user", user
        try:
            return (user[0]['id'], user[0]['first_name'], user[0]['last_name'])
        except:
            return False
