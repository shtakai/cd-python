from system.core.model import Model
import re
import bcrypt

class Review(Model):
    def __init__(self):
        super(Review, self).__init__()

    def get_reviews(self, req):
        query = 'select reviews.*, books.*, users.id as user_id, users.alias as user_alias, users.name as user_name from reviews inner join books on books.id = reviews.book_id inner join users on reviews.user_id = users.id order by reviews.updated_at desc limit 3'
        values = {}
        review_result = self.db.query_db(query, values)
        return {
                'status': True,
                'reviews': review_result
                }

    def destroy(self, req, review_id):
        query = 'delete from reviews where id = :review_id'
        values = {
                'review_id': review_id
                }
        review_result = self.db.query_db(query, values)
        return {
                'status': True,
                'review_result': review_result
                }
