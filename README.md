=Proyecto final bases de datos 2 =

= Instalación =

	pip install -r requirements.py

= Configuración =
Editar el archivo config.py con los parámetros de la conexión a la base de datos

= Crear esquema ==
	Loggearse dentro de la base de datos y ejecutar:
	start oracleSQL/EsquemaFinal.sql

= Poblar DB ==
	Ejecutar:
	python populate_db.py

= Arrancar el servidor =
	python2 server.py

