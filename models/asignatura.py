from config import Config


class Asignatura:

    tabla = "asignaturas"

    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre


    @staticmethod
    def create(nombre):
        query = " INSERT INTO %s (id, nombre)  VALUES (sequence_asignaturas.nextval, '%s')" % (Asignatura.tabla, nombre)
        cursor = Config.getCursor()
        try:
            cursor.execute(query)
            cursor.execute("select sequence_asignaturas.currval from DUAL")
        except Exception, e:
            print e
            print query
            print "No es posible guardar objeto"
            return None
        id = cursor.fetchone()[0]
        return Asignatura(id, nombre)


    @staticmethod
    def getById(id):
        cursor = Config.getCursor()
        query = "SELECT * FROM %s WHERE id=%s" % (Asignatura.tabla, id)
        try:
            cursor.execute(query)
            row = cursor.fetchone()  
        except:
            print "No es posible ejecutar query  o no hay resultados validos"
            return None
        return Asignatura(row[0], row[1])


    @staticmethod
    def getAll():
        cursor = Config.getCursor()
        query = "SELECT * FROM %s " % Asignatura.tabla
        try:
            cursor.execute(query)
        except:
            print "No es posible ejecutar query  o no hay resultados validos"
            return []
        asignaturas  = []
        rows = cursor.fetchall()
        for row in rows:
            asignaturas.append(Asignatura(row[0], row[1]))
        return asignaturas
