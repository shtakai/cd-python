from system.core.model import Model
import re

class Comment(Model):
    def __init__(self):
        super(Comment, self).__init__()


    def get_comments(self, message_id):
        query = "select comments.*, users.id as author_id, users.first_name, users.last_name from comments inner join users on comments.user_id = users.id where message_id = :message_id order by updated_at desc"
        values = {
                'message_id': message_id
                }
        comments = self.db.query_db(query, values)
        return {
                'status': True,
                'comments': comments
                }


    def create(self, req, user_id):
        print 'create start',req, user_id
        query = "insert into comments (message_id, user_id, comment, created_at, updated_at) values (:message_id, :user_id, :comment, NOW(), NOW())"
        values = {
                'message_id': req['message_id'],
                'user_id': user_id,
                'comment': req['comment']
                }
        result = self.db.query_db(query, values)
        print "8888888 result", result
        return {
                'status': True,
                'result': result
                }

