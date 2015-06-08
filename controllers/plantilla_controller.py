__author__ = 'null3d'
from models.plantilla import Plantilla
import web
render = web.template.render('templates/', base="base")

class ListarPlantilla:
    def GET(self):
        #import ipdb; ipdb.set_trace()
        plantillas = Plantilla.getAll()
        return render.listar_plantillas (plantillas)


class CrearPlantilla:

    def GET(self):
        datos = web.input()
        if 'plantilla_base' in datos:
            preguntas = Plantilla.getById(plantilla_base).preguntas
            return render.crear_plantilla_desde_base(preguntas)
        else:
            datos = None
            return render.crear_plantilla(datos)

    def POST(self):
        datos_in = web.input()
        nombre = datos_in['nombre']
        # Guardar todas las preguntas
        #departamento = datos_in['departamento']
        #pais = datos_in['pais']
        #c = Ciudad.create(ciudad, departamento, pais)
        raise web.redirect('/plantilla/listar/')


class VerPlantilla:

    def GET(self):
        datos = web.input()
        #print datos
        #import ipdb; ipdb.set_trace()
        id_plantilla = datos['id']
        plantilla = Plantilla.getById(id_plantilla)
        return render.ver_plantilla(plantilla)
    #Collect id plantilla
    def POST(self):
        datos_in = web.input()
        nombre = datos_in['id']
        # Guardar todas las preguntas
        #departamento = datos_in['departamento']
        #pais = datos_in['pais']
        #c = Ciudad.create(ciudad, departamento, pais)
        raise web.redirect('/plantilla/listar/')
