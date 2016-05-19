from system.core.router import routes

routes['default_controller'] = 'Quotes'
routes['GET']['/quotes/index_json'] = 'Quotes#index_json'
routes['GET']['/quotes/index_html'] = 'Quotes#index_html'
routes['POST']['/quotes/create'] = 'Quotes#create'
