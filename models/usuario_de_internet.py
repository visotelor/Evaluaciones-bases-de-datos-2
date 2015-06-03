from config import Config
from models.usuario import Usuario
from ciudad import Ciudad
from models.orden import Orden

class Usuario_de_internet:

    tabla = "usuarios_de_internet"

    def __init__(self, identificador, sexo, fecha_nacimiento, direccion_despacho, dr_ciudad_id, telefono):
        self.id = identificador
        self.sexo = sexo #F/M (uppercase)
        self.fecha_nacimiento = fecha_nacimiento #formato postgresql ANIO-MES-DIA
        self.direccion_despacho = direccion_despacho
        self.dr_ciudad_id = dr_ciudad_id
        self.telefono = telefono

    
    #actualizar
    def save(self):
        query = "UPDATE  %s SET sexo='%s', fecha_nacimiento='%s', direccion_despacho='%s', dr_ciudad_id=%d telefono =%d WHERE id=%d" % (Usuario_de_internet.tabla, self.sexo, self.fecha_nacimiento, self.direccion_despacho, self.dr_ciudad_id, self.telefono,self.id)
        cursor = Config.getCursor()
        try:
            cursor.execute(query)
        except Exception, e:
            print e
            print "No es posible actualizar el registro"
            return None
        return self
    
    def getCity(self):
        return Ciudad.getById(self.dr_ciudad_id)

    #insertar
    @staticmethod
    def create(identificador,sexo, fecha_nacimiento, direccion_despacho, dr_ciudad_id, telefono):
        if Usuario.getById(identificador) == None :
            print "El usuario no existe, no se puede crear el Usuario_de_internet"
            return None;
        else:
            query = " INSERT INTO %s (id, sexo, fecha_nacimiento, direccion_despacho, dr_ciudad_id, telefono) VALUES (%s,'%s','%s','%s',%s,%s)  RETURNING id " % (Usuario_de_internet.tabla, str(int(identificador)), sexo, fecha_nacimiento, direccion_despacho,str(int(dr_ciudad_id)), str(int(telefono)))
            cursor = Config.getCursor()
            try:
                cursor.execute(query)
            except Exception, e:
                print e 
                print "No es posible guardar objeto"
        id = cursor.fetchone()
        #crear orden
        Orden.create(id[0])
        return Usuario_de_internet(id[0],sexo, fecha_nacimiento, direccion_despacho, dr_ciudad_id, telefono)

    #consultar - obtiene los atributos unicos del usuario de internet
    @staticmethod
    def getById(id):
        cursor = Config.getCursor()
        query = "SELECT * FROM %s WHERE id=%d" % (Usuario_de_internet.tabla, id)
        try:
            cursor.execute(query)
            row = cursor.fetchone()  
        except Exception, e:
            print e
            print "No es posible ejecutar query  o no hay resultados validos"
            return None
        if row == None: #si no se encuentra ningun registro
            return None         
        return Usuario_de_internet(row['id'], row['sexo'], row['fecha_nacimiento'], row['direccion_despacho'], row['dr_ciudad_id'], row['telefono'])
    
    #consultar todos - obtiene los atributos unicos del usuario de internet
    @staticmethod
    def getAll():
        cursor = Config.getCursor()
        query = "SELECT * FROM %s " % Usuario_de_internet.tabla
        try:
            cursor.execute(query)
        except Exception, e:
            print e
            print "No es posible ejecutar query  o no hay resultados validos"
            return []
        usuarios  = []
        rows = cursor.fetchall()
        for row in rows:
            usuarios.append(Usuario_de_internet(row['id'], row['sexo'], row['fecha_nacimiento'], row['direccion_despacho'], row['dr_ciudad_id'], row['telefono']))
        return usuarios

    #consultar el usuario - obtiene los atributos de usuario 
    @staticmethod
    def getUser(id):
        usuario = Usuario.getById(id)
        if usuario == None :
            print "El usuario no existe,"
            return None;
        return usuario
    
    # como es usuario_de_internet entonces se obtiene la ciudad de despacho
    @staticmethod
    def obtenerCiudad(id):
        cursor = Config.getCursor()
        query = "SELECT ciudades.nombre FROM usuarios_de_internet JOIN ciudades ON usuarios_de_internet.dr_ciudad_id = ciudades.id WHERE usuarios_de_internet.id = %d" %id
        try:
            cursor.execute(query)
        except Exception, e:
            print e
            print "No es posible ejecutar query  o no hay resultados validos"
            return []
        row = cursor.fetchone()
        direccion = row['nombre'] # toma el nombre de la columna que dio como resultado
        return direccion