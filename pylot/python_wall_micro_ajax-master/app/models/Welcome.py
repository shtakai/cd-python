
from system.core.model import Model

class Welcome(Model):
    def __init__(self):
        super(Welcome, self).__init__()

    def login(self, req):
        query = "SELECT users.id, users.email, concat(first_name, ' ',last_name) as name FROM users where email = :email"
        values = {
        "email":req['email']
        }
        temp_user = self.db.query_db(query,values)
        # if else statement
        try:
            temp_user[0]

            if self.bcrypt.check_password_hash(temp_user[0]['password'], req['password']):
                return (temp_user[0]['id'], temp_user[0]['name'])
            else:
                return False

        except:
            return False
    def messages_index(self):
        query = 'select messages.id as m_id, messages.message, messages.created_at as m_c_at, concat(users.first_name," ", users.last_name) as m_author from messages left join users on messages.users_id = users.id'
        values = {}
        return self.db.query_db(query,values)
    def comments_index(self):
        query = 'select comments.id as c_id, comments.comment, comments.created_at as c_c_at,comments.messages_id as m_id, concat(users.first_name," ", users.last_name) as c_author from comments left join users on comments.users_id = users.id'
        values = {}
        return self.db.query_db(query,values)
    def register(self, req):
        print ("*"*50)
        for key,value in req.items():
            if len(value) == 0:
                return False
        print ("*"*50)
        password = self.bcrypt.generate_password_hash(req['password'])
        query = 'insert into users (first_name, last_name, email, password, created_at, updated_at) VALUES (":first name", ":last name", ":email", ":password", NOW(),NOW())'
        values = {
            'first_name':req['first_name'],
            'last_name':req['last_name'],
            'email':req['email'],
            'password':password
            }
        user = self.db.query_db(query,values)
        try:
            user[0]
            return (user[0]['id'], user[0]['first_name'], user[0]['last_name'])
        except:
            return False
        return "hello"
