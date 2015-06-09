from models.usuario import Usuario
from models.evaluacion import Evaluacion
from models.plantilla import Plantilla
#from models.administrador import Administrador
import web


render = web.template.render('templates/', base="base")

class ListarUsuarios:
    def GET(self):
        datos = {}
        datos['administradores'] = Administrador.getAll()
        datos['despachadores'] = Despachador.getAll()
        datos['usuarios'] = Usuario_de_internet.getAll()
        return render.listar_usuarios (datos)


class CrearEvaluacion:

    def GET(self):
    	datos = web.input()
        #datos['ciudades'] = Ciudad.getAll()
        return render.crear_evaluacion(datos) 

    def POST(self):
        datos_in = web.input()
        periodo = datos_in['periodo']
        fecha_final = datos_in['fecha_final']
        fecha_inicial = datos_in['fecha_inicial']
        tiempo_maximo = datos_in ['tiempo_maximo']
        plantilla_id= datos_in['plantilla_id']
        evaluacion = Evaluacion.create(periodo, fecha_final, fecha_inicial, tiempo_maximo, plantilla_id)
        raise web.redirect('/evaluacion/ver/')


class VerEvaluacion:

    def GET(self):
        datos = web.input()
        #import ipdb; ipdb.set_trace()
        id_evaluacion = datos['id']
        evaluacion = Evaluacion.getById(id_evaluacion)

        plantillaid = datos['plantilla']
        preguntas = Plantilla.getPreguntas(plantillaid)
        return render.ver_evaluacion(evaluacion,preguntas)
    #Collect id plantilla
    def POST(self):
        datos_in = web.input()
        nombre = datos_in['id']
        # Guardar todas las preguntas
        #departamento = datos_in['departamento']
        #pais = datos_in['pais']
        #c = Ciudad.create(ciudad, departamento, pais)
        raise web.redirect('/plantilla/listar/')

 