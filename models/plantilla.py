from config import Config
from models.pregunta import Pregunta

class Plantilla:

    tabla = "plantillas"
    tabla_preguntas_plantillas = "plantillas_preguntas"

    def __init__(self, id, nombre, modificable="Y", eliminada="N"):
        self.id = id
        self.nombre = nombre
        self.modificable = modificable
        self.eliminada = eliminada
        self.preguntas = self.getPreguntas(id)


    @staticmethod
    def create(nombre, modificable="Y", eliminada="N"):
        query = " INSERT INTO %s (id, nombre, modificable, eliminada)  VALUES (sequence_plantillas.nextval, '%s', '%s', '%s')" % (Plantilla.tabla, nombre, modificable, eliminada)
        cursor = Config.getCursor()
        try:
            cursor.execute(query)
            cursor.execute("select sequence_plantillas.currval from DUAL")
        except Exception, e:
            print e
            print query
            print "No es posible guardar objeto"
            return None
        row = cursor.fetchone()[0]
        return Plantilla(row, nombre, modificable, eliminada)

    @staticmethod
    def create(nombre):
        modificable="Y"
        eliminada="N"
        query = " INSERT INTO %s (id, nombre, modificable, eliminada)  VALUES (sequence_plantillas.nextval, '%s', '%s', '%s')" % (Plantilla.tabla, nombre, modificable, eliminada)
        cursor = Config.getCursor()
        try:
            cursor.execute(query)
            cursor.execute("select sequence_plantillas.currval from DUAL")
        except Exception, e:
            print e
            print query
            print "No es posible guardar objeto"
            return None
        row = cursor.fetchone()[0]
        return Plantilla(row, nombre, modificable, eliminada)

    def addPregunta(self, pregunta):
        p = Pregunta.create(pregunta)
        cursor = Config.getCursor()
        if not p: 
            return False
        try:
            query =  "INSERT INTO %s (plantilla_id, pregunta_id) VALUES (%s, %s)" % (Plantilla.tabla_preguntas_plantillas, self.id, p.id)
            cursor.execute(query)
            return True
        except Exception, e:
            print e
            print query
            print "No es posible guardar la relacion"
            return False


    @staticmethod #id plantilla
    def getPreguntas(id):
        query = "SELECT pr.id, pr.pregunta FROM %s tr, %s pr, %s pl WHERE tr.plantilla_id=pl.id AND pr.id=tr.pregunta_id AND pl.id=%s" % (Plantilla.tabla_preguntas_plantillas, Pregunta.tabla, Plantilla.tabla, id)
        cursor = Config.getCursor()
        preguntas = [] 
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                print row
                preguntas.append(Pregunta(row[0], row[1]))
            return preguntas
        except Exception, e:
            print query
            print e
            return []


    @staticmethod
    def getById(id):
        cursor = Config.getCursor()
        query = "SELECT * FROM %s WHERE id=%s" % (Plantilla.tabla, id)
        try:
            cursor.execute(query)
            row = cursor.fetchone() 
        except:
            print "No es posible ejecutar query  o no hay resultados validos"
            return None
        return Plantilla(row[0], row[1], row[2], row[3])


    @staticmethod
    def getAll():
        cursor = Config.getCursor()
        query = "SELECT * FROM %s " % Plantilla.tabla
        try:
            cursor.execute(query)
        except:
            print "No es posible ejecutar query  o no hay resultados validos"
            return []
        plantillas  = []
        rows = cursor.fetchall()
        for row in rows:
            plantillas.append(Plantilla(row[0], row[1], row[2], row[3]))
        return plantillas
