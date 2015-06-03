from config import Config
from models.usuario import Usuario

class Administrador:

	tabla = "administradores"

	def __init__(self, identificador):
		self.id = identificador
		self.privilegios = Usuario.getTipo(self.id)
	'''
	#actualizar (se puede actualizar un administrador actualizando como usuario)
	def save(self):
		query = "UPDATE  %s SET  nombre_completo='%s', usuario='%s', contrasena='%s', e_mail='%s', dr_ciudad_id =%s WHERE id=%s" % (Usuario.tabla, self.nombre_completo, self.usuario, self.contrasena,self.e_mail,self.dr_ciudad_id,self.id)
		cursor = Config.getCursor()
		try:
			cursor.execute(query)
		except Exception, e:
			print e
			print "No es posible actualizar el registro"
			return None
		return self
    '''
	#insertar (anade la clave del primaria usuario  como clave foranea en administradores)
	@staticmethod
	def create(identificador): #del usuario
		if Usuario.getById(identificador) == None :
			print "El usuario no existe, no se puede crear el administrador"
			return None;
		else:	
			query = " INSERT INTO %s (id) VALUES (%s)  RETURNING id " % (Administrador.tabla, str(int(identificador)))
			cursor = Config.getCursor()
			try:
				cursor.execute(query)
			except Exception, e:
				print e
				print "No es posible guardar objeto"
			id = cursor.fetchone()
		return Administrador(id[0])

	#consultar por id
	@staticmethod
	def getById(id):
		cursor = Config.getCursor()
		query = " SELECT * FROM %s JOIN %s ON %s.id = %s.id WHERE %s.id=%d" % (Administrador.tabla,Usuario.tabla,Administrador.tabla,Usuario.tabla,Administrador.tabla,id)
		try:
			cursor.execute(query)
			row = cursor.fetchone()  
		except Exception, e:
			print e
			print "No es posible ejecutar query o no hay resultados validos"
			return None
		if row == None: #si no se encuentra ningun registro
			return None			
		return Usuario(row['id'], row['nombre_completo'], row['usuario'], row['contrasena'], row['e_mail'],row['direccion_residencia'], row['dr_ciudad_id'])
	
	#consultar todos
	@staticmethod
	def getAll():
		cursor = Config.getCursor()
		query = "SELECT * FROM %s JOIN %s ON %s.id = %s.id" % (Administrador.tabla,Usuario.tabla,Usuario.tabla, Administrador.tabla)
		try:
			cursor.execute(query)
		except Exception, e:
			print e
			print "No es posible ejecutar query  o no hay resultados validos"
			return []
		usuarios  = []
		rows = cursor.fetchall()
		for row in rows:
			usuarios.append(Usuario(row['id'], row['nombre_completo'], row['usuario'], row['contrasena'], row['e_mail'],row['direccion_residencia'], row['dr_ciudad_id']))
		return usuarios

	#consulta para nombre o e_email o nombre_completo (criterio de busqueda, texto de busqueda)
	@staticmethod
	def getAllWith(criterio,entrada):
		cursor = Config.getCursor()
		query = "SELECT * FROM %s JOIN %s ON %s.id = %s.id WHERE %s.%s='%s'" % (Administrador.tabla,Usuario.tabla,Administrador.tabla,Usuario.tabla,Usuario.tabla,criterio,entrada)
		try:
			cursor.execute(query)
		except Exception, e:
			print e
			print "No es posible ejecutar query  o no hay resultados validos"
			return []
		usuarios  = []
		rows = cursor.fetchall()
		for row in rows:
			usuarios.append(Usuario(row['id'], row['nombre_completo'], row['usuario'], row['contrasena'], row['e_mail'],row['direccion_residencia'], row['dr_ciudad_id']))
		return usuarios
