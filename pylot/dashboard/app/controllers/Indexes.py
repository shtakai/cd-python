from system.core.controller import *
from time import strftime
import datetime
import string
import random

class Indexes(Controller):
    def __init__(self, action):
        super(Indexes, self).__init__(action)

    def index(self):
        return self.load_view('/index.html')
