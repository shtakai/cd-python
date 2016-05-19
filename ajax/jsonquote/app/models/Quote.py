from system.core.model import Model
import re
import bcrypt

class Quote(Model):
    def __init__(self):
        super(Quote, self).__init__()

    def all(self):
        query = 'select * from quotes'
        return self.db.query_db(query)

