from typing import Text
from pyttsx3 import engine, speak
import pyttsx3

from .date import DateToday

class SpeechAssistant():

	def __init__(self):
		self.__engine = pyttsx3.init()
		
		voices = self.__engine.getProperty('voices')
		self.__engine.setProperty('voice', voices[0].id)
		rate = self.__engine.getProperty('rate')
		self.__engine.setProperty('rate', 150)

		self.__datetoday = DateToday()


	def speak(self, audio):
<<<<<<< HEAD
		self.__engine.say(audio)
		self.__engine.runAndWait()

	def date(self):
		self.hour = self.__datetoday.getDatetoday()
		text = f'hoy es {self.dateTime["weekday"]} {self.dateTime["day"]} de {self.dateTime["month"]} del {self.dateTime["year"]}'
		speak(text)

	def timeNow(self):
		self.hour = self.__datetoday.getHour()
		text = f'son las, {self.hour}'
		speak(text)
=======
		try: 
			self.__engine.say(audio)
			self.__engine.runAndWait()
		except Exception as e:
			print(e)

	def date(self):
		try: 
			self.hour = self.__datetoday.getDatetoday()
			text = f'hoy es {self.dateTime["weekday"]} {self.dateTime["day"]} de {self.dateTime["month"]} del {self.dateTime["year"]}'
			speak(text)
		except Exception as e:
			print(e)

	def timeNow(self):
		try: 
			self.hour = self.__datetoday.getHour()
			text = f'son las, {self.hour["hour"]} y {self.hour["minute"]}'
			speak(text)
		except Exception as e:
			print(e)

>>>>>>> Asistente_1.0.2
