from system.core.model import Model
import re
import bcrypt

class Post(Model):
    def __init__(self):
        super(Post, self).__init__()

    def get_all_posts(self):
        print 'Post#get_all_posts'
        query = 'select * from posts order by updated_at desc'
        posts_result = self.db.query_db(query, {})
        print 'posts_result', posts_result
        return {
                'status': True,
                'result': posts_result
                }

    def create(self,req):
        print 'Post#create', req
        query = 'insert into posts (description, created_at, updated_at) values (:description, NOW(), NOW())'
        values = {
                'description': req['description']
                }
        post_result = self.db.query_db(query, values)
        return {
                'status': True,
                'result': post_result
                }
