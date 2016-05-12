from system.core.model import Model

class Course(Model):
    def __init__(self):
        super(Course, self).__init__()

    def index(self):
        query = "SELECT * FROM courses"
        print query
        print "index"
        return self.db.query_db(query)

    def show(self,params): # int of an id.
        print params, "FROM COURSES"
        query = "SELECT * FROM courses WHERE id = {}".format(params)
        print query
        return self.db.query_db(query)

    def delete(self,params):
        query = "DELETE FROM courses WHERE id = {}".format(params)
        print query
        self.db.query_db(query)
        return "delete "

    def create(self, params):
        print params, " THESE ARE IN THE MODEL"
        query = "INSERT INTO courses (Title, Description, created_at, updated_at) VALUES ('{}', '{}', NOW(), NOW())".format(params['Title'],params['Description'])
        print query
        self.db.query_db(query)
        return "create"


    def update(self,params):
        query ="UPDATE courses SET Title = '{}', Description = '{}' WHERE id = {}".format(params)
        print query
        self.db.query_db(query)
        return "update"
