import os
from database.database import getAplicacionByName

def abrirAplicacion(nombre):
	try:
		ruta = getAplicacionByName(str(nombre))
		for i in ruta:
			exe_dir = str(i[2]).split(sep='\\')
			print(exe_dir)
			comando = 'start ' + exe_dir[(len(exe_dir) - 1)]
			app = comando.split('.exe')
			print(app)
			
			os.system(app[0])

	except Exception as e:
		print(e)
