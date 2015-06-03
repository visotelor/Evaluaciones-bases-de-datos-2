#Cristian Alejandro Rojas
#carojasq@correo.udistrital.edu.co

#El presente archivo define los parametros de conexion a la base de datos y devuelve un objeto cursor para hacer las consultas SQL con el
#CREATE USER db2 IDENTIFIED by db2;
#GRANT CONNECT TO db2;


ADMIN_USER = "db2"
ADMIN_PASSWORD = "db2"

import cx_Oracle
import psycopg2
import psycopg2.extensions
import psycopg2.extras
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE) # Unicode support


class Config:
	@staticmethod
	def getCursor(username = ADMIN_USER, password=ADMIN_PASSWORD, host="null3d", port="1521"):
		#Se definen los parametros de conexion a la base de host
		try:
			conn = cx_Oracle.connect('%s/%s@%s:%s/XE' % (username, password, str(host), str(port)))
			try: 
				conn.autocommit = True
			except:
				print "No fue posible poner autocommit en su conexion, por favor revise los parametros de configuracion de su base de datos"
		except Exception, e:
			print e 
			print "Se produjo un error en la conexion con la base de datos"
			quit()
		cursor = conn.cursor()  # Return querys as dicts
		return cursor


