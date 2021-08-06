
from os import getpid
from components.abrirAplicacion import abrirAplicacion
from components.abrirPagina import abrirPagina
from database.database import getReuniones, getPalabrasByType
from components.speechAsistente import SpeechAssistant
import unicodedata
from components.listenAsistente import ListenAssistent
from components.abrirReunion import abrirReunion
from components.buscarYoutube import buscarMusica
from components.search import buscar
from components.wikipedia import consulta


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
				break

		self.palabraMusica = getPalabrasByType('musica')
		for i in self.palabraMusica:
			if unicodedata.normalize('NFKD', i[1]).encode('ASCII', 'ignore').strip().upper() == unicodedata.normalize('NFKD', query).encode('ASCII', 'ignore').strip().upper():
				SpeechAssistant().speak('que cancion quiere reproducir')
				musica = ListenAssistent().listen()
				SpeechAssistant().speak('buscando cancion')
				buscarMusica(musica)
				break

		self.palabraBusqueda = getPalabrasByType('busqueda')
		for i in self.palabraBusqueda:
			if unicodedata.normalize('NFKD', i[1]).encode('ASCII', 'ingonre').strip().upper() == unicodedata.normalize('NFKD', query).encode('ASCII', 'ignore').strip().upper():
				SpeechAssistant().speak('que quiere buscar')
				busqueda = ListenAssistent().listen()
				SpeechAssistant().speak('realizando busqueda')
				buscar(busqueda)
				break


		self.palabraConsulta = getPalabrasByType('consulta')
		for i in self.palabraConsulta:
			if unicodedata.normalize('NFKD', i[1]).encode('ASCII', 'ingonre').strip().upper() == unicodedata.normalize('NFKD', query).encode('ASCII', 'ignore').strip().upper():
				SpeechAssistant().speak('que desea consultar')
				consult = ListenAssistent().listen()
				SpeechAssistant().speak('de acuerdo a wikipedia')		
				datos = consulta(consult)
				print(datos)
				SpeechAssistant().speak(datos)
				break






