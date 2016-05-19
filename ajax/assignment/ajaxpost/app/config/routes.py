from system.core.router import routes

routes['default_controller'] = 'Posts'
routes['POST']['/notes/create_html'] = 'Posts#create_html'

# routes['GET']['/users/show/<id>'] = 'Users#show'
