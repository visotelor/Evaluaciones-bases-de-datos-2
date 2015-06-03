from models.producto import Producto
from models.ciudad import Ciudad
from models.usuario import Usuario
from models.usuario_de_internet import Usuario_de_internet
from controllers.login import logged
import web

render = web.template.render('templates/', base="base")

class CatalogoProductos:

    def GET(self):
        print "inside GET!"
        #import ipdb; ipdb.set_trace()
        print web.ctx.session.privilege
        print web.ctx.session.login
        #import ipdb; ipdb.set_trace()
        if logged():
            print "logged!"
            user = Usuario_de_internet.getById(web.ctx.session.privilege)
            ciudad_id =  user.dr_ciudad_id
            print user
            print ciudad_id
            productos = Producto.getByCity(ciudad_id)
            return render.catalogo_productos(productos,user=user)
        else:
            raise web.redirect('/login')


    def POST(self):
        if logged():
            user = Usuario_de_internet.getById(web.ctx.session.privilege)
            ciudad_id =  user.dr_ciudad_id
            busqueda = web.input()['search']
            productos = Producto.getByCity(ciudad_id, name_like=busqueda)
            return render.catalogo_productos(productos, user=user)

        else:
            render.login_error();