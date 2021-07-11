import webbrowser
from database.database import getReunionesByName



def abrirReunion(nombre):
	try:
		reunion = getReunionesByName(nombre)
		for i in reunion:
			webbrowser.open(i[2])

	except Exception as e:
		print(e)