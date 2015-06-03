from models.proveedor import Proveedor
import web

render = web.template.render('templates/', base="base")

class ListarProveedores:

    def GET(self):
        proveedores = Proveedor.getAll()
        return render.listar_proveedores (proveedores)


class CrearProovedor:

    def GET(self):
        from models.ciudad import Ciudad
        datos = {}
        datos['ciudades'] = Ciudad.getAll()
        return render.crear_proveedor(datos)                                      

    def POST(self):
        datos_in = web.input()
        nombre = datos_in['nombre']
        direccion = datos_in['direccion']
        ciudad_id = datos_in['ciudad']
        c =  Proveedor.create(nombre, direccion, ciudad_id)
        raise web.redirect('/proveedores/listar/')
