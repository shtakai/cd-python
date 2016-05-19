from system.core.model import Model
import re
import bcrypt

class Quote(Model):
    def __init__(self):
        super(Quote, self).__init__()

    def all(self):
        query = 'select * from quotes'
        return self.db.query_db(query)

    def create(self, new_quote):
        print 'Quote#create', new_quote
        query = 'insert into quotes (quote, author) values (:quote, :author)'
        values ={
                'quote': new_quote['quote'],
                'author': new_quote['author']
                }
        quote_result = self.db.query_db(query, values)

        return quote_result

