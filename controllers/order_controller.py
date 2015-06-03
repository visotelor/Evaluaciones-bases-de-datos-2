from models.producto import Producto
from controllers.login import logged
from models.usuario_de_internet import Usuario_de_internet
from models.orden import Orden
import web

render = web.template.render('templates/', base="base")
class VerOrdenesPrevias():
    def GET(self):
        #import ipdb; ipdb.set_trace() 
        ordenes=Orden.getPrevias(web.ctx.session.privilege)
        return render.ver_ordenes_previas(ordenes)

class VerCarrito:
    def GET(self):
        order = Orden.getCarrito(web.ctx.session.privilege)
        user = Usuario_de_internet.getById(web.ctx.session.privilege)
        order_lines = order.getLineas(user.dr_ciudad_id)
        total = 0
        for ol in order_lines:
            total += ol['cantidad'] + ol['precio']
        return render.carrito(order_lines, total=total, user=user)


class AnadirProducto:
    def POST(self):
        #import ipdb; ipdb.set_trace()
        mensaje = "Producto agregado!"
        user = Usuario_de_internet.getById(web.ctx.session.privilege)
        datos = web.input()
        producto_id = int(datos['producto_id'])
        cantidad  = int(datos['cantidad'])
        order = Orden.getCarrito(web.ctx.session.privilege)
        order.anadirProducto(producto_id, cantidad)
        web.seeother("/carrito/")


class CheckOutCarrito:
    def POST(self):
        #import ipdb; ipdb.set_trace()
        from models.producto import Producto
        datos = web.input()
        medio_de_pago = datos['medio_de_pago']
        user = Usuario_de_internet.getById(web.ctx.session.privilege)
        dr_ciudad_id = user.dr_ciudad_id
        order = Orden.getCarrito(user.id)
        order.medio_de_pago = medio_de_pago
        order_lines = order.getLineas(user.dr_ciudad_id)
        total = 0
        for ol in order_lines:
            Producto.getById(ol['product_id']).reducirEnCiudad(dr_ciudad_id, ol['cantidad'])
            total += ol['cantidad'] + ol['precio']
        order.total= total
        order.save()
        Orden.create(web.ctx.session.privilege)
        web.seeother("/carrito/")