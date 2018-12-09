import os
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

_here=os.path.dirname((os.path.realpath(__file__)))


def assajos(request):
    return{
    	'titol':'Assajos','titol2':'Assistència Assajos'
    }

def diades(request):
	return{
    	'titol':'Diades','titol2':'Registre Diades'
    	
	}
if __name__ == '__main__':
    config = Configurator()
    config.include('pyramid_chameleon')
    config.add_route('assajos', '/assajos.html')
    config.add_view(assajos, route_name='assajos',renderer=_here+'/plantilla1.pt')
    config.add_route('diades','/diades.html')
    config.add_view(diades, route_name='diades',renderer=_here+'/plantilla1.pt')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
    pyramid.includes = pyramid_chameleon