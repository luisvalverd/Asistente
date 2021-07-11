import webbrowser
from database.database import getPaginasByName

def abrirPagina(nombre):
	try:
		pagina = getPaginasByName(nombre)
		for i in pagina:
			webbrowser.open(i[2])

	except Exception as e:
		print(e)


