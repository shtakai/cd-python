from system.core.controller import *
from time import strftime
import datetime
import string
import random

class Comments(Controller):
    def __init__(self, action):
        super(Comments, self).__init__(action)
        self.load_model('Comment')

    def create(self):
        print 'create start', request.form
        result = self.models['Comment'].create(request.form, session['user'])

        print 'result ****', result
        print 'redirect userid', request.form['target_user_id']
        return redirect("/users/show/{}".format(request.form['target_user_id']))
