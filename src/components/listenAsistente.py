import speech_recognition as sr

class ListenAssistent():
	def __init__(self):
		self.__listen = sr.Recognizer()
	
	def listen(self):
		with sr.Microphone() as source:
			print('listen...')
			self.__listen.pause_threshold = 1
			audio = self.__listen.listen(source)
			try:
				print('grabando...')
				query = self.__listen.recognize_google(audio, language='es-Ec')
				return query

			except Exception as e:
				print(e)