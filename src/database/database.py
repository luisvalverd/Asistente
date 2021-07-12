import psycopg2

pg = psycopg2.connect(database="asistentevirtual", user="postgres", password="mhgygjlop2")

cursor = pg.cursor()

def getPalabrasByType(tipo):
	cursor.execute("SELECT * FROM palabras_claves WHERE tipo_palabra = %(tipo)s", {'tipo': tipo})
	palabras = cursor.fetchall()
	return palabras

def getReuniones():
	cursor.execute("SELECT * FROM reuniones")
	reuniones = cursor.fetchall()
	return reuniones

def getReunionesByName(nombre):
	cursor.execute("SELECT * FROM reuniones WHERE nombre = %(nombre)s", {'nombre': nombre})
	reunion = cursor.fetchall()
	return reunion

def InserReunion(nombre, url):
	cursor.execute("INSERT INTO reuniones(nombre, url) VALUES (%(nombre)s, %(url)s)", {'nombre': nombre, 'url': url})
	pg.commit()

def DeleteReunion(nombre):
	cursor.execute("DELETE FROM reuniones WHERE nombre = %(nombre)s", {'nombre': nombre})
	pg.commit()

def getPaginas():
	cursor.execute("SELECT * FROM paginasweb")
	paginas = cursor.fetchall()
	return paginas

def getPaginasByName(nombre):
	cursor.execute("SELECT * FROM paginasweb WHERE nombre = %(nombre)s", {'nombre': nombre})
	pagina = cursor.fetchall()
	return pagina

def InsertPagina(nombre, url):
	cursor.execute("INSERT INTO paginasweb(nombre, url) VALUES (%(nombre)s, %(url)s)", {'nombre': nombre, 'url': url})
	pg.commit()

def DeletePagina(nombre):
	cursor.execute("DELETE FROM reuniones WHERE nombre = %(nombre)s", {'nombre': nombre})
	pg.commit()

def getAplicaciones():
	cursor.execute("SELECT * FROM aplicaciones")
	aplicaciones = cursor.fetchall()
	return aplicaciones

def getAplicacionByName(nombre):
	cursor.execute("SELECT * FROM aplicaciones WHERE nombre = %(nombre)s", {'nombre': nombre})
	aplicacion = cursor.fetchall()
	return aplicacion

def InsertAplicacion(nombre, ruta):
	cursor.execute("INSERT INTO aplicaciones(nombre, path) VALUES (%(nombre)s, %(ruta)s)", {'nombre': nombre, 'ruta': ruta})
	pg.commit()

def DeleteAplicacion(nombre):
	cursor.execute("DELETE FROM aplicaciones WHERE nombre = %(nombre)s", {'nombre': nombre})
	pg.commit()
	


