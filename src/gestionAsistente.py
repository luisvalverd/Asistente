
from components.abrirAplicacion import abrirAplicacion
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
				SpeechAssistant().speak('abriendo reunión')
				abrirReunion(str(reunion))
				break

		self.palabraPagina = getPalabrasByType('pagina')
		for i in self.palabraPagina:
			if unicodedata.normalize('NFKD', i[1]).encode('ASCII', 'ignore').strip().upper() == unicodedata.normalize('NFKD', query).encode('ASCII', 'ignore').strip().upper():
				SpeechAssistant().speak('que pagina quiere abrir')
				pagina = ListenAssistent().listen()
				SpeechAssistant().speak('abriendo página web')
				abrirPagina(str(pagina))
				break
		
		self.palabraAplicacion = getPalabrasByType('aplicacion')
		for i in self.palabraAplicacion:
			if unicodedata.normalize('NFKD', i[1]).encode('ASCII', 'ignore').strip().upper() == unicodedata.normalize('NFKD', query).encode('ASCII', 'ignore').strip().upper():
				SpeechAssistant().speak('que aplicación quiere abrir')
				aplicacion = ListenAssistent().listen()
				SpeechAssistant().speak('abriendo aplicación')
				abrirAplicacion(str(aplicacion))








