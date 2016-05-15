"""
    Sample Model File

    A Model should be in charge of communicating with the Database.
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
import re

class Product(Model):
    def __init__(self):
        super(Product, self).__init__()


    def get_products(self):
        query = "select * from products order by updated_at desc"
        values = {}
        products = self.db.query_db(query, values)
        return {
                'status': True,
                'products': products
                }


    def create_product(self, req):
        pass

    def get_product(self, id, req):
        pass

    def update_product(self, id, req):
        pass

    def destroy_product(self, req):
        pass



    # def post_comment(self, req, user_id):
        # query = "insert into comments (comment, user_id, message_id, created_at, updated_at) values (:comment, :user_id, :message_id, NOW(), NOW())"
        # values = {
                # 'comment' : req['comment'],
                # 'user_id' : user_id,
                # 'message_id': req['message_id']
                # }
        # result = self.db.query_db(query, values)

        # return {
            # 'status': True,
            # 'result': result
            # }


