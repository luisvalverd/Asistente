from pyttsx3 import speak
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import imp
import speech_recognition

image = imp.load_source('image_rc.py', r'.\views\image_rc.py')

class App(QMainWindow):

	def __init__(self):
		super().__init__()
		uic.loadUi("views\Main.ui", self)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	windows = App()
	windows.show()
	sys.exit(app.exec_())