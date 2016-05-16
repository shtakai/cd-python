"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes

"""
    This is where you define routes

    Start by defining the default controller
    Pylot will look for the index method in the default controller to handle the base route

    Pylot will also automatically generate routes that resemble: '/controller/method/parameters'
    For example if you had a products controller with an add method that took one parameter
    named id the automatically generated url would be '/products/add/<id>'
    The automatically generated routes respond to all of the http verbs (GET, POST, PUT, PATCH, DELETE)
"""
routes['default_controller']            = 'Indexes'
routes['GET']['/'] = 'Indexes#index'
routes['GET']['/login'] = 'Users#sign_in'
routes['GET']['/register'] = 'Users#sign_up'
routes['POST']['/register'] = 'Users#register'
routes['POST']['/login'] = 'Users#login'
routes['GET']['/dashboard/admin'] = 'Users#dashboard_admin'
routes['GET']['/users/show/<id>'] = 'Users#show'
routes['GET']['/users/edit/<id>'] = 'Users#edit'
routes['POST']['/users/update_user'] = 'Users#update_user'
routes['POST']['/users/update_password'] = 'Users#update_password'

