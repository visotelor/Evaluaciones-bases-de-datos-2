from models.usuario import Usuario
from config import Config

class Tesis:

    tabla = "tesis"

    def __init__(self, id, nombre, jurado=None, director=None):
        self.id = id
        self.nombre = nombre
        self.jurado = self.getJurado()
        self.director = self.getDirector()

    @staticmethod
    def create(nombre):
        query = " INSERT INTO %s (id, nombre) VALUES (sequence_tesis.nextval, '%s')" % (Tesis.tabla, str(nombre))
        cursor = Config.getCursor()
        try:
            cursor.execute(query)
            cursor.execute("select sequence_tesis.currval from DUAL")
        except Exception, e:
            print e
            print "No es posible guardar objeto"
        id = cursor.fetchone()
        return Tesis(id[0],nombre)

    def setDirector(self, director):
        return True

    def setJurado(self, jurado):
        return True

    def getJurado(self):
        return None

    def getDirector(self):
        return None

    @staticmethod
    def getById(id):
        return True
