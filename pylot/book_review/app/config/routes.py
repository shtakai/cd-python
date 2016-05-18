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
routes['GET']['/reviews/delete/<id>'] = 'Reviews#destroy'
