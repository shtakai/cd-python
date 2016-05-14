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
        query = 'select * from users where email = :email limit 1'
        value = {
                'email': req['email'],
                }
        try:
            tmp_user = self.db.query_db(query, value)
            print 'tmp_user', tmp_user

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

        query = "insert into users (first_name, last_name, email, pw_hash,  created_at, updated_at) values (:first_name, :last_name, :email, :password, NOW(),NOW())"
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
            print "okay"
            print user
            return user
        except:
            return False



    def get_messages(self):
        messages = []
        query = "select messages.*, users.first_name, users.last_name from messages inner join users on messages.user_id = users.id order by id asc"
        values = {}
        result = self.db.query_db(query, values)
        for m in result:
            print m['id']
            query = "select comments.*, users.first_name, users.last_name from comments inner join users on comments.user_id = users.id where comments.message_id = :message_id order by comments.id asc"
            values = {
                    'message_id': m['id']
                    }
            comments = self.db.query_db(query, values)
            messages.append({
                'message': m,
                'comments': comments
                })
        print messages
        return messages

    def post_message(self, req, user_id):
        print "-" * 10
        print "req", req
        print "user_id", user_id
        query = "insert into messages (message, user_id, created_at, updated_at) values (:message, :user_id, NOW(), NOW())"
        values = {
                'message' : req['message'],
                'user_id' : user_id
                }
        result = self.db.query_db(query, values)
        print result
        return result


    def post_comment(self, req, user_id):
        print "-" * 10
        print "req", req
        print "user_id", user_id
        query = "insert into comments (comment, user_id, message_id, created_at, updated_at) values (:comment, :user_id, :message_id, NOW(), NOW())"
        values = {
                'comment' : req['comment'],
                'user_id' : user_id,
                'message_id': req['message_id']
                }
        result = self.db.query_db(query, values)
        print result
        return result


