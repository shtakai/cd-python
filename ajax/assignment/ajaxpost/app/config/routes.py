from system.core.router import routes

routes['default_controller'] = 'Posts'
routes['POST']['/notes/create_html'] = 'Posts#create_html'
routes['POST']['/notes/create'] = 'Posts#create'

# routes['GET']['/users/show/<id>'] = 'Users#show'
