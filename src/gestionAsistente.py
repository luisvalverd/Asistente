<<<<<<< HEAD

class Gestion():
	def __init__(self):
		self.__query = ''

	def reconocer(self, query):
		if query == 'Hola':
			print('ok')
=======
from components.abrirPagina import abrirPagina
from database.database import getReuniones, getPalabrasByType
from components.speechAsistente import SpeechAssistant
import unicodedata
from components.listenAsistente import ListenAssistent
from components.abrirReunion import abrirReunion

""" reconocer voz del usuario """

class Gestion():
	def __init__(self):
		pass

	def reconocer(self, query):
		self.palabrasHora = getPalabrasByType('hora')
		for i in self.palabrasHora:
			if unicodedata.normalize('NFKD', i[1]).encode('ASCII', 'ignore').strip().upper() == unicodedata.normalize('NFKD', query).encode('ASCII', 'ignore').strip().upper():
				SpeechAssistant().timeNow()
				break

		self.palabraReunion = getPalabrasByType('reunion')
		for i in self.palabraReunion:
			if unicodedata.normalize('NFKD', i[1]).encode('ASCII', 'ignore').strip().upper() == unicodedata.normalize('NFKD', query).encode('ASCII', 'ignore').strip().upper():
				SpeechAssistant().speak('que reunion quiere abrir')
				reunion = ListenAssistent().listen()
				SpeechAssistant().speak('abriendo reunion')
				abrirReunion(str(reunion))
				break

		self.palabraPagina = getPalabrasByType('pagina')
		for i in self.palabraPagina:
			if unicodedata.normalize('NFKD', i[1]).encode('ASCII', 'ignore').strip().upper() == unicodedata.normalize('NFKD', query).encode('ASCII', 'ignore').strip().upper():
				SpeechAssistant().speak('que pagina quiere abrir')
				pagina = ListenAssistent().listen()
				SpeechAssistant().speak('abriendo pagina web')
				abrirPagina(str(pagina))
				




>>>>>>> Asistente_1.0.2


