from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.i18n import TranslationStringFactory
from pyramid.response import Response
import datetime

_=TranslationStringFactory('penjats')

inscrits = [
	{'nom': 'David',
	'Diada':'Emboirats',
	'sortida': '14:10',
	'tornada': '22:15',
	'cotxe': 'no'},
	{'nom': 'Pau',
	'Diada': 'Penjats',
	'sortida': '14:00',
	'tornada': '23:30',
	'cotxe': 'si'}
]


inscritsA = [
	{'nom': 'David',
	'DatesAssaig': 'dimarts 2',
	'Arribada': '13:30',
	'Sortida': '15,30'},
	{'nom': 'Oriol',
	'DatesAssaig': 'dijous 11',
	'Arribada': '14:00',
	'Sortida': '15:00'}
	]

DatesAssaig = ['dimarts 2','dijous 4','dimarts 9','dijous 11','dimarts 16','dijous 18','dimarts 23','dijous 25','dimarts 30']
DatesDiades = ['Grillats','Emboirats','Penjats','Bergants','Llunatics']

Esdeveniments = [{'text': "Espai de proves", 'data': datetime.datetime(2017,5,5,12,0)},{'text':"Diada cultural:\nLa colla organitzarà la diada cultural del dia 27 d'abril. Entre altres actes hi celebrarem una diada castellera amb els emboirats de la UVic com a colla convidada.",'data':datetime.datetime(2017,5,8,12,40)}]

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'penjats'}

@view_config(route_name='assistencia', renderer='templates/assistencia.pt')
def assistencia(request):
    return {'project': 'penjats','esdeveniments':Esdeveniments}

@view_config(route_name='diades', renderer='templates/diades.pt')
def diades(request):

	if request.method == 'POST':
		usuari= {}
		usuari['nom'] = request.params['nom']
		usuari['Diada'] = request.params['Diada']
		usuari['sortida'] = request.params['sortida']
		usuari['tornada'] = request.params['tornada']
		usuari['cotxe'] = request.params['cotxe']
		inscrits.append(usuari)
		return HTTPFound(location='confirmacio.html')
    	
	return {	
	'titol': _('Diades'),
	'titol2': _('Registre diades'),
	'project': 'penjats',
	'llista_dates_diada': DatesDiades}

@view_config(route_name='assajos', renderer='templates/assajos.pt')
def assajos(request):
	if request.method == 'POST':
		usuariA = {}
		usuariA['nom'] = request.params['nom']
		usuariA['DatesAssaig'] = request.params['DatesAssaig']
		usuariA['Arribada'] = request.params['Arribada']
		usuariA['Sortida'] =request.params['Sortida']
		inscritsA.append(usuariA)
		return HTTPFound(location='confirmacio.html')
    	
	return {
	'titol': _('Assajos'),
	'titol2': _('Assistència assajos'),
    'project': 'penjats',
    'llista_dates_assaig': DatesAssaig}

@view_config(route_name='confirmacio', renderer='templates/confirmacio.pt')
def confirmacio(request):
    return {
    'titol': _('Confirmació'),
	'titol2': _('Confirmació assistència'),
    'project': 'penjats'}


@view_config(route_name='admin', renderer='templates/admin.pt')
def admin(request):



	if request.method == 'POST':
		new_event= {}
		Diada = request.params['Diada']
		if len(Diada)>1:
			DatesDiades.append(Diada)
		Assaig = request.params['Assaig']
		if len(Assaig)>1:
			DatesAssaig.append(Assaig)
		event = request.params['event']
		if len(event)>1:
			new_event['text']=request.params['event']
			new_event['data']= datetime.datetime.now()
			Esdeveniments.append(new_event)
		return HTTPFound(location='confirmacio.html')

	inscrits_filtre = inscrits
	inscrits_filtre_A =inscritsA
	if request.method == 'GET':
		Diada = request.params.get('Diada')
		Assaig = request.params.get('Assaig')
		if Diada:
			inscrits_filtre = [inscrit for inscrit in inscrits if inscrit['Diada']==Diada]
		if Assaig:
			inscrits_filtre_A = [inscrit for inscrit in inscritsA if inscrit['DatesAssaig']==Assaig]


	return {'titol': 'Admin',
	'titol2': 'Panell administració',
	'project': 'penjats',
	'inscrits': inscrits_filtre,
	'inscritsA':inscrits_filtre_A,
	'llista_dates_diada': DatesDiades,
	'llista_dates_assaig': DatesAssaig}

@view_config(route_name='esdeveniments', renderer='templates/esdeveniments.pt')
def esdeveniments(request):
    return {
    'titol': _('Esdeveniments'),
	'titol2': _('Confirmació assistència'),
    'project': 'penjats',
    'esdeveniments':Esdeveniments}

@view_config(route_name='canvia_idioma')
def canvia_idioma(request):
	request.response.set_cookie('_LOCALE_',request.params['idioma'], max_age=None, path='/')
	request.response.location ='/'
	request.response.status_int = 303
	return request.response

@view_config(route_name='llista_diades')
def llista_diades(request):
	return Response("""<option value="Grillats">Grillats (4 de maig)</option>
		  	<option value="Emboirats">Emboirats (11 de maig)</option>
		  	<option value="Penjats">Penjats (18 de maig)</option>
		  	<option value="Bergants">Bergants (25 de maig)</option>
			<option value="Llunatics">Llunatics dinàmics(1 de juny)</option>""")

@view_config(route_name='llista_assajos')
def llista_assajos(request):
	return Response("""<option value="Dimarts 2">Dimarts 2</option>
			<option value="Dijous 4">Dijous 4</option>
			<option value="Dimarts 9">Dimarts 9</option>
			<option value="Dijous 11">Dijous 11</option>""")

@view_config(route_name='llista_events')
def llista_events(request):
	return Response("""esdeveniments""")