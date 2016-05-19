from system.core.controller import *
from time import strftime
import datetime
import string
import random
import re

class Posts(Controller):
    def __init__(self, action):
        super(Posts, self).__init__(action)
        self.load_model('Post')

    # helper methods
    def set_flash(self, messages, level):
        for message in messages:
            flash(message, level)

    def index(self):
        print 'Posts#index', request.form
        posts_result = self.models['Post'].get_all_posts()
        print 'posts_result', posts_result
        return self.load_view('/index.html', posts=posts_result['result'])

    def create_html(self):
        print 'Posts#create_html', request.form
        post_result = self.models['Post'].create(request.form)
        print 'post_result', post_result
        return redirect('/')
