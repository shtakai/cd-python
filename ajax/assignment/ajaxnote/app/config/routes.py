from system.core.router import routes

routes['default_controller'] = 'Notes'
routes['GET']['/notes'] = 'Notes#index_json'
routes['GET']['/notes/new'] = 'Notes#new'
routes['POST']['/notes/create'] = 'Notes#create'
routes['POST']['/notes/update/<int:id>'] = 'Notes#update'
routes['POST']['/notes/delete/<int:id>'] = 'Notes#destroy'
# routes['POST']['/notes/create_html'] = 'Posts#create_html'
# routes['POST']['/notes/create'] = 'Posts#create'

# routes['GET']['/users/show/<id>'] = 'Users#show'
