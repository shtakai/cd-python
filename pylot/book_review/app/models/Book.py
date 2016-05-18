from system.core.model import Model
import re
import bcrypt

class Book(Model):
    def __init__(self):
        super(Book, self).__init__()

    def get_books_simple(self, req):
        query = 'select books.id, books.title, count(*) as review_count from books inner join reviews on books.id = reviews.book_id group by books.id order by reviews.updated_at desc'
        values = {}
        book_result = self.db.query_db(query, values)
        return {
                'status': True,
                'books': book_result
                }

    def create(self, req, user_id):
        errors = []
        if not req['book_title'] and not req['author']:
            errors.append('Book title can\'t be empty')
        if not req['review']:
            errors.append('Review can\'t be empty')
        if not req['rating']:
            errors.append('Rating can\'t be empty')
        if not req['author'] and not req['new_author']:
            errors.append('Author or New author should be exist')
        if errors:
            return {
                    'status': False,
                    'errors': errors
                    }
        # check new author exist?
        # NOTE:There are no transactions.
        if req.get('new_author'):
            query = 'select * from authors where name = :name limit 1'
            values = {
                    'name': req['new_author']
                    }
            author_result = self.db.query_db(query, values)
            if not author_result:
                query = 'insert into authors (name, created_at, updated_at) values (:name, NOW(), NOW())'
                values = {
                        'name': req['new_author']
                        }
                author_result = [{u'id':self.db.query_db(query, values)}]

        else:
            query = 'select * from authors where name = :name limit 1'
            values = {
                    'name': req['new_author']
                    }
            author_result = self.db.query_db(query, values)

        author_id = req['author'] if req['author'] else author_result[0]['id']
        # create book
        query = 'insert into books (title, author_id, created_at, updated_at) values (:title, :author_id, NOW(), NOW())'
        values = {
                'title': req['book_title'],
                'author_id': author_id
                }
        book_result = self.db.query_db(query, values)

        # guard: denied book insertion
        if not book_result:
            errors.append('error happened on creating book')
            return {
                'status': False,
                'errors': errors
                }

        book_id = book_result
        # create review
        query = 'insert into reviews (user_id, book_id, review, rating, created_at, updated_at) values (:user_id, :book_id, :review, :rating, NOW(), NOW())'
        values = {
            'user_id': user_id,
            'book_id': book_id,
            'review': req['review'],
            'rating': req['rating']
            }
        review_result = self.db.query_db(query, values)
        return {
                'status': True,
                'book': book_result,
                'review': review_result,
                'author': author_result
                # 'user': user_result
                }

    def get_book(self, book_id):
        # get book info w/author
        query = 'select books.id, books.title, books.author_id, authors.name as author_name from books inner join authors on books.author_id = authors.id where books.id = :book_id limit 1'
        values = {
                'book_id': book_id
                }
        book_result = self.db.query_db(query, values)
        if not book_result:
            return {
                    'status': False
                    }

        # get 3 reviews w/user
        query = 'select reviews.*, users.alias from reviews inner join users on reviews.user_id = users.id where reviews.book_id = :book_id order by reviews.updated_at desc limit 3'
        values = {
                'book_id': book_id
                }
        review_result = self.db.query_db(query, values)
        return {
                'status': True,
                'book_result': book_result[0],
                'review_result': review_result
                }
