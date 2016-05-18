from system.core.model import Model
import re
import bcrypt

class Author(Model):
    def __init__(self):
        super(Author, self).__init__()


    def get_all_authors(self, req):
        query = 'select * from authors order by updated_at desc'
        values = {}
        author_result = self.db.query_db(query, values)
        return {
                'status': True,
                'authors': author_result
                }


