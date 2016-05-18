from system.core.router import routes

routes['default_controller'] = 'Users'
routes['POST']['/users/register'] = 'Users#register'
routes['POST']['/users/login'] = 'Users#login'
routes['GET']['/logout'] = 'Users#logout'
routes['GET']['/books'] = 'Books#index'
routes['GET']['/books/add'] = 'Books#new'
routes['POST']['/books/create'] = 'Books#create'
routes['GET']['/users/<id>'] = 'Users#show'
routes['GET']['/books/<id>'] = 'Books#show'

# routes['default_controller']            = 'Indexes'
# routes['GET']['/'] = 'Indexes#index'
# routes['GET']['/login'] = 'Users#sign_in'
# routes['GET']['/logout'] = 'Users#logout'
# routes['GET']['/register'] = 'Users#sign_up'
# routes['POST']['/register'] = 'Users#register'
# routes['POST']['/login'] = 'Users#login'
# routes['GET']['/dashboard/admin'] = 'Users#dashboard_admin'
# routes['GET']['/users/show/<id>'] = 'Users#show'
# routes['GET']['/users/edit/<id>'] = 'Users#edit'
# routes['POST']['/users/update_user_admin'] = 'Users#update_user_admin'
# routes['POST']['/users/update_password_admin'] = 'Users#update_user_password_admin'
# routes['POST']['/users/destroy'] = 'Users#destroy'
# routes['GET']['/users/new'] = 'Users#new'
# routes['POST']['/messages/create'] ='Messages#create'
# routes['POST']['/comments/create'] ='Comments#create'
