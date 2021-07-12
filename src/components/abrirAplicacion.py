import os
from database.database import getAplicacionByName

def abrirAplicacion(nombre):
	try:
		ruta = getAplicacionByName(str(nombre))
		for i in ruta:
			exe_dir = str(i[2]).split(sep='\\')
			comando = 'start ' + exe_dir[(len(exe_dir) - 1)]
			os.system(comando)

	except Exception as e:
		print(e)
