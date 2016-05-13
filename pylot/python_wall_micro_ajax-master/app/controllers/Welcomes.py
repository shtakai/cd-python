
from system.core.controller import *

class Welcomes(Controller):
    def __init__(self, action):
        super(Welcomes, self).__init__(action)

        self.load_model('Welcome')
        self.db = self._app.db

    def index(self):
        return self.load_view('welcome/index.html')

    def login(self):
        # go to model, check validations and then return user or errors
        user = self.models['Welcome'].login(request.form)
        if user:
            #tuple unpacking
            session['id'],session['name']  = user
        # print request.form
        # the wall -- is what we want to load
            return redirect('/messages')
        return redirect('/')

    def register(self):
        user = self.models['Welcome'].register(request.form)
        if len(user) == 3:
            session['id'] = user[0]
            session['name'] = user[1]+" "+user[2]
            return redirect('/messages')
        return redirect('/')

    def messages_index(self):
        messages = self.models['Welcome'].messages_index()
        comments = self.models['Welcome'].comments_index()
        return self.load_view('welcome/theWall.html', comments = comments, messages = messages)

    def messages_ajax(self):
        messages = self.models['Welcome'].messages_index()
        comments = self.models['Welcome'].comments_index()
        return self.load_view('partials/_messages.html', comments = comments, messages = messages)

    def newusersajax(self):
        return self.load_view('partials/_login.html')
