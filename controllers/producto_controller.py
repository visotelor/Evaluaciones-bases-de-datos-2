from models.producto import Producto
from controllers.login import logged
from models.usuario_de_internet import Usuario_de_internet
import web

render = web.template.render('templates/', base="base")

class ListarProductos:

    def GET(self):
        productos = Producto.getAll()
        return render.listar_productos (productos)


class CrearProducto:

    def GET(self):
        from models.categoria import Categoria
        from models.proveedor import Proveedor
        datos = {}
        datos['categorias'] = Categoria.getAll()
        datos['proveedores'] = Proveedor.getAll()
        return render.crear_producto(datos)                                      

    def POST(self):
        datos_in = web.input()
        nombre = datos_in['nombre']
        caracteristicas = datos_in['caracteristicas']
        # TODO foto to base 64
        foto = datos_in['foto']
        marca = datos_in['marca']
        existencia_minima = int(datos_in['existencia_minima'])
        proveedor_id = int(datos_in['proveedor_id'])
        categoria_id = int(datos_in['categoria_id'])
        p =  Producto.create(nombre, caracteristicas, foto, marca, existencia_minima, proveedor_id, categoria_id)
        raise web.redirect('/productos/listar/')

class ConsultarProducto:
    def GET(self):
        get_input = web.input()
        product_id = int(get_input['id'])
        user = Usuario_de_internet.getById(web.ctx.session.privilege)
        precio = Producto.getPrecio(product_id,user.dr_ciudad_id)
        producto = Producto.getById(product_id)
        datos = {}
        datos['producto'] = producto
        datos['precio'] = precio
        #import ipdb; ipdb.set_trace()
        return render.info_producto(datos)                                      


        

