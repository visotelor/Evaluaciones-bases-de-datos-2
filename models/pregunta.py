from config import Config


class Pregunta:

    tabla = "preguntas"

    def __init__(self, id, pregunta):
        self.id = str(id)
        self.pregunta = pregunta


    @staticmethod
    def create(pregunta):
        query = " INSERT INTO %s (id, pregunta)  VALUES (sequence_preguntas.nextval, '%s')" % (Pregunta.tabla, pregunta)
        cursor = Config.getCursor()
        try:
            cursor.execute(query)
            cursor.execute("select sequence_preguntas.currval from DUAL")
        except Exception, e:
            print e
            print query
            print "No es posible guardar objeto"
            return None
        id = cursor.fetchone()[0]
        return Pregunta(id, pregunta)


    @staticmethod
    def getById(id):
        cursor = Config.getCursor()
        query = "SELECT * FROM %s WHERE id=%s" % (Pregunta.tabla, id)
        try:
            cursor.execute(query)
            row = cursor.fetchone()  
        except:
            print "No es posible ejecutar query  o no hay resultados validos"
            return None
        return Pregunta(row[0], row[1])


    @staticmethod
    def getAll():
        cursor = Config.getCursor()
        query = "SELECT * FROM %s " % Pregunta.tabla
        try:
            cursor.execute(query)
        except:
            print "No es posible ejecutar query  o no hay resultados validos"
            return []
        preguntas  = []
        rows = cursor.fetchall()
        for row in rows:
            cargos.append(Pregunta(row[0], row[1]))
        return preguntas
