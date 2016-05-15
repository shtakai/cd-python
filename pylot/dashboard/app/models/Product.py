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
        number_pattern = r"^\d+$"
        if not re.match(number_pattern, req['price']):
            return {
                    'status': False,
                    'messages': ["Price must be number"]
                    }
        query = "insert into products (name, description, price, created_at, updated_at) values (:name, :description, :price, NOW(), NOW())"
        values = {
                'name': req['name'],
                'description': req['description'],
                'price': req['price']
                }
        product = self.db.query_db(query, values)
        result = {
                'status': True,
                'product': product
                }
        return result

    def get_product(self, id):
        query = "select * from products where id = :id limit 1"
        values = {
                'id': id
                }
        product = self.db.query_db(query, values)
        result = {
                'status': True,
                'product': product[0]
                }
        return result

    def update_product(self, id, req):
        number_pattern = r"^\d+$"
        if not re.match(number_pattern, req['price']):
            return {
                    'status': False,
                    'messages': ["Price must be number"]
                    }
        query = "update products set name=:name, description = :description, price = :price, updated_at = NOW() where id = :id"
        values = {
                'id': id,
                'name': req['name'],
                'description': req['description'],
                'price': req['price']
                }
        product = self.db.query_db(query, values)
        result = {
                'status': True,
                'product': product
                }
        return product

    def destroy_product(self, req):
        query = "delete from products where id = :id"
        values = {
                'id': req['id']
                }
        product = self.db.query_db(query, values)
        result = {
                'status': True,
                'product': product
                }
        return product

