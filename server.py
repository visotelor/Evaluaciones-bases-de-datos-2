import web
web.config.debug = False
from controllers.ciudad_controller import *
from controllers.categoria_controller import *
from controllers.proveedor_controller import *
from controllers.producto_controller import *
from controllers.usuario_controller import *
from controllers.catalogo_productos import *
from controllers.index_controller import *
from controllers.order_controller import *
from controllers.admin_controller import *
from controllers.login import *
from controllers.reset import *


# Aca se definen las URLs (url, nombre controlador)
urls = (
    '/', 'IndexController',
    '/index', 'IndexController',
    '/login','Login',
    '/reset','Reset',
    '/ciudad/crear/.*', 'CrearCiudad',
    '/categoria/crear/.*', 'CrearCategoria',
    '/ciudad/listar/.*', 'ListarCiudades',
    '/categoria/listar/.*', 'ListarCategorias',
    '/proveedores/listar/.*', 'ListarProveedores',
    '/proveedor/crear/.*', 'CrearProovedor',
    '/productos/listar/.*', 'ListarProductos',
    '/producto/crear/.*', 'CrearProducto',
    '/usuario/listar/.*', 'ListarUsuarios',
    '/usuario/crear/.*', 'CrearUsuario',
    '/producto/ver/.*','ConsultarProducto',
    '/catalogo/.*', 'CatalogoProductos',
    '/orden/anadir/.*', 'AnadirProducto',
    '/orden/previas/.*', 'VerOrdenesPrevias',
    '/carrito/checkout/.*', 'CheckOutCarrito',
    '/carrito/.*', 'VerCarrito',
    '/admin/.*', 'VerAdmin',
)

render = web.template.render('templates/', base="base")


app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'login': 0, 'privilege': 0})

def session_hook():
    web.ctx.session = session
    web.template.Template.globals['session'] = session

app.add_processor(web.loadhook(session_hook))
app.run()




