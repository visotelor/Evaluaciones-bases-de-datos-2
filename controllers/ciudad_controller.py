from models.ciudad import Ciudad
import web

render = web.template.render('templates/', base="base")

class ListarCiudades:
    def GET(self):
        ciudades = Ciudad.getAll()
        return render.listar_ciudades (ciudades)


class CrearCiudad:

    def GET(self):
    	datos = None
        return render.crear_ciudad(datos)                                      

    def POST(self):
        datos_in = web.input()
        ciudad = datos_in['ciudad']
        departamento = datos_in['departamento']
        pais = datos_in['pais']
        c = Ciudad.create(ciudad, departamento, pais)
        raise web.redirect('/ciudad/listar/')
