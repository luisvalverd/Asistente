from importlib import import_module
from PyQt5 import QtWidgets
from pyttsx3 import speak
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import imp
from components.speechAsistente import SpeechAssistant
from components.date import DateToday
from components.listenAsistente import ListenAssistent
from views.reuniones import Ui_Frame
from gestionAsistente import Gestion
from views.paginasWeb import Ui_PaginasWeb

image = imp.load_source('image_rc.py', r'.\views\image_rc.py')

class App(QMainWindow):

	def __init__(self):
		super().__init__()
		uic.loadUi("views\Main.ui", self)
		self.speak = SpeechAssistant()
		self.button = self.listenButton
		self.reunionesB = self.reunionesButton
		self.paginasB = self.paginasButton

		self.paginasB.clicked.connect(self.gestionPaginasWeb)
		self.button.clicked.connect(self.onClick)
		self.reunionesB.clicked.connect(self.gestionReuniones)
		

	def onClick(self):
		try:
			self.listen = ListenAssistent().listen()
			print(self.listen)
			self.funicion = Gestion().reconocer(self.listen)

		except Exception as e:
			print(e)

	def gestionReuniones(self):
		try:
			self.reuniones = QMainWindow()
			self.ui = Ui_Frame()
			self.ui.setupUi(self.reuniones)
			self.reuniones.show()

		except Exception as e:
			print(e)

	def gestionPaginasWeb(self):
		try:
			self.paginas = QMainWindow()
			self.ui = Ui_PaginasWeb()
			self.ui.setupUi(self.paginas)
			self.paginas.show()
		except Exception as e:
			print(e)

	def greatings(self):
		try: 
			self.timeNow = DateToday().getHour()
			if int(self.timeNow["hour"]) > 4 and int(self.timeNow["hour"]) < 12:
				self.speak.speak('Buenos dias en que puedo ayudarte?')
			elif int(self.timeNow["hour"]) > 12 and int(self.timeNow["hour"]) < 18:
				self.speak.speak('Buenas tardes en que puedo ayudarte?')
			else:
				self.speak.speak('Buenas noches en que puedo ayudarte?')
		
		except Exception as e:
			print(e)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	windows = App()
	windows.show()
	windows.greatings()
	sys.exit(app.exec_())