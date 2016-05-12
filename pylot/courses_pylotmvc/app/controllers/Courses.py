"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        self.load_model('Course')

    def index(self):
        courses = self.models['Course'].index();
        return self.load_view('index.html', courses = courses)

    def destroy_confirm(self, id):
        #print(id, "our id")
        course = self.models['Course'].show(int(id))
        # returns a list of length 1.
        #print course
        # go to db and call show
        return self.load_view('delete_confirm.html', course = course[0])

    def create(self):
        print request.form
        arguments = {"Title": request.form['Title'],"Description": request.form['Description']}
        self.models['Course'].create(arguments)

        return redirect('/return')


    def delete(self,id):
        print self.models['Course'].delete(int(id))
        #call to DB and delete.
        return redirect('/return')
