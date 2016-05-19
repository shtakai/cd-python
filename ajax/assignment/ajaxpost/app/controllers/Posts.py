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
        return self.load_view('/index.html')

