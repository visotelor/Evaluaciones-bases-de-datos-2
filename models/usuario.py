from config import Config


#Este modelo es de otro proyecto, hay que adaptarlo para las necesidades
class Usuario:

    tabla = "usuarios"

    def __init__(self, identificador, nombre_completo, usuario, contrasena, e_mail, direccion_residencia):
        self.id = identificador
        self.nombre_completo = nombre_completo
        self.usuario = usuario
        self.contrasena = contrasena
        self.e_mail = e_mail
        self.privilegios = Usuario.getTipo(self.id)

    #actualizar
    def save(self):
        query = "UPDATE  %s SET  nombre_completo='%s', usuario='%s', contrasena='%s', e_mail='%s', direccion_residencia='%s' dr_ciudad_id =%d WHERE id=%s" % (Usuario.tabla, self.nombre_completo, self.usuario, self.contrasena,self.e_mail,self.direccion_residencia,self.dr_ciudad_id,self.id)
        cursor = Config.getCursor()
        try:
            cursor.execute(query)
        except Exception, e:
            print e
            print "No es posible actualizar el registro"
            return None
        return self

    #insertar
    @staticmethod
    def create(identificador,nombre_completo, usuario, contrasena, e_mail,direccion_residencia,dr_ciudad_id):
        query = " INSERT INTO %s (id, nombre_completo, usuario, contrasena, e_mail,direccion_residencia, dr_ciudad_id) VALUES (%s,'%s','%s','%s','%s','%s', %s)  RETURNING id " % (Usuario.tabla, str(int(identificador)), nombre_completo, usuario, contrasena, e_mail,direccion_residencia, str(int(dr_ciudad_id)))
        cursor = Config.getCursor()
        try:
            cursor.execute(query)
        except Exception, e:
            print e
            print "No es posible guardar objeto"
        id = cursor.fetchone()
        return Usuario(id[0],nombre_completo, usuario, contrasena, e_mail,direccion_residencia, dr_ciudad_id)
    
    #consultar
    @staticmethod
    def getById(id):
        cursor = Config.getCursor()
        query = "SELECT * FROM %s WHERE id=%s" % (Usuario.tabla, id)
        try:
            cursor.execute(query)
            row = cursor.fetchone()  
        except Exception, e:
            print e
            print "No es posible ejecutar query  o no hay resultados validos"
            return None
        if row == None: #si no se encuentra ningun registro
            return None         
        return Usuario(row['id'], row['nombre_completo'], row['usuario'], row['contrasena'], row['e_mail'], row['direccion_residencia'], row['dr_ciudad_id'])

    #consultar todos
    @staticmethod
    def getAll():
        cursor = Config.getCursor()
        query = "SELECT * FROM %s " % Usuario.tabla
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

    #consulta para usuario o e_email o nombre_completo (criterio de busqueda, texto de busqueda)
    @staticmethod
    def getAllWith(criterio,entrada):
        cursor = Config.getCursor()
        query = "SELECT * FROM %s WHERE %s='%s'" % (Usuario.tabla,criterio,entrada)
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

    # obtener ciudad de residencia 
    @staticmethod
    def obtenerCiudad(id):
        cursor = Config.getCursor()
        query = "SELECT ciudades.nombre FROM usuarios JOIN ciudades ON usuarios.dr_ciudad_id = ciudades.id WHERE usuarios.id = %s" %id
        try:
            cursor.execute(query)
        except Exception, e:
            print e
            print "No es posible ejecutar query  o no hay resultados validos"
            return []
        row = cursor.fetchone()
        ciudad = row['nombre'] # toma el nombre de la columna que dio como resultado
        return ciudad

    @staticmethod
    def getTipo(id):
        cursor = Config.getCursor()
        query = "SELECT id FROM usuarios_de_internet WHERE id=%d" %id
        try:
            cursor.execute(query)
        except Exception, e:
            print e
            print "No es posible ejecutar query  o no hay resultados validos"
            return []
        resultado = []
        row = cursor.fetchone()
        if row != None:
            resultado.append("Usuario de internet")

        query = "SELECT id FROM administradores WHERE id=%d" %id
        try:
            cursor.execute(query)
        except Exception, e:
            print e
            print "No es posible ejecutar query  o no hay resultados validos"
            return []
        row = cursor.fetchone()
        if row != None:
            resultado.append("Administrador")

        query = "SELECT id FROM despachadores WHERE id=%d" %id
        try:
            cursor.execute(query)
        except Exception, e:
            print e
            print "No es posible ejecutar query  o no hay resultados validos"
            return []
        row = cursor.fetchone()
        if row != None:
            resultado.append("Despachador")
        return resultado