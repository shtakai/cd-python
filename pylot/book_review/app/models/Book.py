from system.core.model import Model
import re
import bcrypt

class Book(Model):
    def __init__(self):
        super(Book, self).__init__()

    def get_books_simple(self, req):
        print "Book#get_books_simple start", req
        query = 'select id, title from books order by updated_at desc'
        values = {}
        book_result = self.db.query_db(query, values)
        print 'book_result', book_result

        return {
                'status': True,
                'books': book_result
                }
