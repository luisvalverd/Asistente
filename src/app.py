from importlib import import_module
from pyttsx3 import speak
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import imp
from components.speechAsistente import SpeechAssistant
from components.date import DateToday
from components.listenAsistente import ListenAssistent
from gestionAsistente import Gestion

image = imp.load_source('image_rc.py', r'.\views\image_rc.py')

class App(QMainWindow):

	def __init__(self):
		super().__init__()
		uic.loadUi("views\Main.ui", self)
		self.speak = SpeechAssistant()
		self.button = self.listenButton

		self.button.clicked.connect(self.onClick)

	def onClick(self):
		try:
			self.listen = ListenAssistent().listen()
			print(self.listen)
			self.funicion = Gestion().reconocer(self.listen)

		except Exception as e:
			print(e)


	def greatings(self):
		self.timeNow = DateToday().getHour()
		if int(self.timeNow["hour"]) > 6 and int(self.timeNow["hour"]) < 12:
			self.speak.speak('Buenos dias en que puedo ayudarte?')
		elif int(self.timeNow["hour"]) > 12 and int(self.timeNow["hour"]) < 18:
			self.speak.speak('Buenas tardes en que puedo ayudarte?')
		else:
			self.speak.speak('Buenas noches en que puedo ayudarte?')


if __name__ == '__main__':
	app = QApplication(sys.argv)
	windows = App()
	windows.show()
	windows.greatings()
	sys.exit(app.exec_())