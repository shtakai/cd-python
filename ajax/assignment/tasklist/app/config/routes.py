from system.core.router import routes

routes['default_controller'] = 'Tasks'
routes['POST']['/tasks/update/<int:id>'] = 'Tasks#update'
routes['POST']['/tasks/create'] = 'Tasks#create'
routes['GET']['/tasks'] = 'Tasks#index_json'
routes['GET']['/tasks/new'] = 'Tasks#new'
# routes['POST']['/notes/create'] = 'Tasks#create'
# routes['POST']['/notes/update/<int:id>'] = 'Tasks#update'
# routes['POST']['/notes/delete/<int:id>'] = 'Tasks#destroy'
