from system.core.model import Model
import re
import bcrypt

class Review(Model):
    def __init__(self):
        super(Review, self).__init__()


    def get_reviews(self, req):
        print 'Review#get_reviews start', req
        query = 'select reviews.*, books.* from reviews inner join books on books.id = reviews.book_id order by reviews.updated_at desc limit 3'
        values = {}
        review_result = self.db.query_db(query, values)
        print 'review_result', review_result

        return {
                'status': True,
                'reviews': review_result
                }


