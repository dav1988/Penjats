from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_translation_dirs('penjats:locale')

    config.add_route('home', '/test')
    config.add_route('assistencia', '/')
    config.add_route('diades', '/diades.html')
    config.add_route('assajos', '/assajos.html')
    config.add_route('confirmacio', '/confirmacio.html')
    config.add_route('admin','/admin.html')
    config.add_route('esdeveniments','/esdeveniments.html')
    config.add_route('canvia_idioma','/canvia_idioma.html')
    config.add_route('llista_diades','llista_diades.html')
    config.add_route('llista_assajos','llista_assajos.html')
    config.add_route('llista_events','llista_events.html')
    config.scan()
    return config.make_wsgi_app()
