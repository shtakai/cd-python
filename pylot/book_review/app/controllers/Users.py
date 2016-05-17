from system.core.controller import *
from time import strftime
import datetime
import string
import random
import re

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')

    # helper methods
    def set_flash(self, messages, level):
        for message in messages:
            flash(message, level)


    def index(self):
        form = {}
        if session.get('user'):
            return redirect('/books')

        return self.load_view('/index.html', form=form)


    def register(self):
        print 'register start', request.form
        print "go"
        result = self.models['User'].register(request.form)

        if result.get('errors'):
            self.set_flash(result['errors'], 'error')
            form = dict(request.form)
            del(form['password'])
            del(form['confirm_password'])
            return self.load_view('/index.html', form=form)

        print 'result', result
        flash('Registration finished. Please Login', 'info')
        return redirect('/')


    def login(self):
        print 'login start', request.form
        result = self.models['User'].login(request.form)
        if result.get('errors'):
            self.set_flash(result['errors'], 'error')
            return redirect('/')

        print 'result', result
        flash('logged in', 'info')
        session['user'] = result['user']
        return redirect('/')

    def logout(self):
        session.clear()
        flash('logged out', 'info')
        return redirect('/')


####################
'''

    def sign_in(self):
        return self.load_view('/users/sign_in.html')

    def sign_up(self):
        return self.load_view('/users/sign_up.html')

    def register(self):

        result = self.models['User'].register(request.form)


        if not result['status']:
            for error in result['errors']:
                flash(error, 'error')
            return self.load_view('/users/sign_up.html', email=request.form['email'], first_name=request.form['first_name'], last_name=request.form['last_name'], description=request.form['description'])
        flash('User registered')
        return redirect('/login')

    def login(self):


        result = self.models['User'].login(request.form)
        if not result['status']:
            for error in result['errors']:
                flash(error, 'error')
            return self.load_view('/users/sign_in.html', email=request.form['email'])


        session['user'] = result['user']
        session['user_name'] = result['user_name']
        session['user_level'] = result['user_level']
        flash('logged in')

        return redirect('/')


    def dashboard_admin(self):
        if not self.is_admin_user():
            flash('disallowed operation', 'error')
            return redirect('/')
        users = self.models['User'].get_all_users()

        return self.load_view('users/dashboard_admin.html',users=users['users'])

    def show(self, id):
        result = self.models['User'].get_user(id)
        if not result['status']:
            flash("user not found")
            return redirect('/')

        user = result['user']

        result = self.models['Message'].get_messages(id)
        messages = []
        for message in result['messages']:
            comments = self.models['Comment'].get_comments(message['id'])
            print 'comments-----', comments
            messages.append({
                'message': message,
                'comments': comments
                })
        print 'messages---', messages



        return self.load_view('users/show.html', user=user, messages=messages)

    def edit(self, id):
        if not self.is_admin_user():
            flash('disallowed operation', 'error')
            return redirect('/')
        result = self.models['User'].get_user(id)
        if not result['status']:
            flash("user not found")
            return redirect('/')
        if result['user']['user_level'] == 9:
            selected_normal = ""
            selected_admin = "selected"
        else:
            selected_normal ="selected"
            selected_admin =""


        return self.load_view('users/edit.html', user=result['user'], selected_normal=selected_normal, selected_admin=selected_admin)



    def update_user_admin(self):
        if not self.is_admin_user():
            flash('disallowed operation', 'error')
            return redirect('/')
        result = self.models['User'].update_user_admin(request.form)
        if not result['status']:
            for error in result['errors']:
                flash(error, 'error')
            user = {
                    'id': request.form['id'],
                    'email': request.form['email'],
                    'first_name': request.form['first_name'],
                    'last_name': request.form['last_name'],
                    'description': request.form['description'],
                    'user_level': request.form['user_level']
                    }
            return self.load_view('/users/edit.html', user=user)

        # users = self.models['User'].get_all_users()
        # return self.load_view('users/dashboard_admin.html',users=users['users'])
        return redirect('/dashboard/admin')

    def is_admin_user(self):
        result = self.models['User'].get_user_info(session['user'])
        if not session['user_level'] or not result or result['user_level'] != 9:
            return False
        else:
            return True

    def update_user_password_admin(self):
        if not self.is_admin_user():
            flash('disallowed operation', 'error')
            return redirect('/')
        result = self.models['User'].update_user_password_admin(request.form)
        if not result['status']:
            for error in result['errors']:
                flash(error, 'error')
            user = result['user']
            return self.load_view('/users/edit.html', user=user)

        print 'updated password'
        return redirect('/dashboard/admin')


    def destroy(self):
        if not self.is_admin_user():
            flash('disallowed operation', 'error')
            return redirect('/')
        print 'destroy start', request.form
        result = self.models['User'].destroy(request.form)
        print 'result', result
        return redirect('/dashboard/admin')


    def new(self):
        if not self.is_admin_user():
            flash('disallowed operation', 'error')
            return redirect('/')
        print 'new start'
        return self.load_view('/users/new.html')

    def create(self):
        if not self.is_admin_user():
            flash('disallowed operation', 'error')
            return redirect('/')
        print 'create start'
        result = self.models['User'].create(request.form)
        print 'result===', result
        if not result['status']:
            for error in result['errors']:
                flash(error, 'error')
            return self.load_view('/users/new.html', email=request.form['email'], first_name=request.form['first_name'], last_name=request.form['last_name'], description=request.form['description'])
        flash('User registered')
        return redirect('/dashboard/admin')

    def logout(self):
        session.clear()
        return redirect('/')
'''
