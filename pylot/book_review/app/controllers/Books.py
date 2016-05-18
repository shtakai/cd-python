from system.core.controller import *
from time import strftime
import datetime
import string
import random
import re

class Books(Controller):
    def __init__(self, action):
        super(Books, self).__init__(action)
        self.load_model('Book')
        self.load_model('User')
        self.load_model('Review')
        self.load_model('Author')

    # helper methods
    def set_flash(self, messages, level):
        for message in messages:
            flash(message, level)

    def redirect_login(self):
        if session['user']:
            return redirect('/')

    def index(self):
        self.redirect_login()
        review_result = self.models['Review'].get_reviews(request.form)
        book_result = self.models['Book'].get_books_simple(request.form)
        return self.load_view('/books/index.html', reviews=review_result['reviews'], books=book_result['books'])

    def new(self):
        self.redirect_login()
        author_result = self.models['Author'].get_all_authors(request.form)
        return self.load_view('/books/new.html', authors=author_result['authors'])

    def create(self):
        self.redirect_login()
        book_result = self.models['Book'].create(request.form, session['user']['id'])
        if not book_result['status']:
            self.set_flash(errors, 'error')
            return redirect('/books/add')

        flash("Added Book and Your Review", 'info')
        return redirect('/books')

    def show(self, id):
        book_result = self.models['Book'].get_book(id)
        if not book_result['status']:
            self.set_flash(book_result['erroes'], 'error')
            return redirect('/')

        return self.load_view('/books/show.html', book=book_result['book_result'], reviews=book_result['review_result'])
