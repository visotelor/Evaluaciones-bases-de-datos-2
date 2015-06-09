#Cristian Alejandro Rojas
#carojasq@correo.udistrital.edu.co

#El presente archivo define los parametros de conexion a la base de datos y devuelve un objeto cursor para hacer las consultas SQL con el
"""
DROP USER db2 CASCADE;
CREATE USER db2 IDENTIFIED by db2;
GRANT CONNECT TO db2;
GRANT RESOURCE TO db2

START /home/null3d/Git_repos/Evaluaciones-bases-de-datos-2/oracleSQL/EsquemaFinal.sql
"""
import cx_Oracle

ADMIN_USER = "vivianadb"
ADMIN_PASSWORD = "viviana"
HOST = "localhost"
PORT  = "1521"

class Config:
	@staticmethod
	def getCursor(username = ADMIN_USER, password=ADMIN_PASSWORD, host=HOST, port=PORT):
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


