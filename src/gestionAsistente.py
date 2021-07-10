from database.database import getReuniones, getPalabrasByType
from components.speechAsistente import SpeechAssistant
import unicodedata

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
			print(i)





