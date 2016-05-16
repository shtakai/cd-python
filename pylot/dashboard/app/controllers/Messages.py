from system.core.controller import *
from time import strftime
import datetime
import string
import random

class Messages(Controller):
    def __init__(self, action):
        super(Messages, self).__init__(action)
        self.load_model('Message')

    def create(self):
        print 'create start', request.form
        result = self.models['Message'].create(request.form, session['user'])


        print 'result ****', result
        return redirect("/users/show/{}".format(request.form['target_user_id']))
