"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
from time import strftime
import datetime

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.

            self.load_model('WelcomeModel')
        """

    """ This is an example of a controller method that will load a view for the client """
    def index(self):
        """
        A loaded model is accessible through the models attribute
        self.models['WelcomeModel'].get_all_users()
        """
        welcome = {
                'mydate': datetime.datetime.now().strftime('%b %d,%Y %I:%m %p')
                }
        return self.load_view('index.html',welcome=welcome)
