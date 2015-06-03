from models.producto import Producto
from models.ciudad import Ciudad
from models.usuario import Usuario
from models.usuario_de_internet import Usuario_de_internet
from controllers.login import logged
import web

render = web.template.render('templates/', base="base")

class VerAdmin:

    def GET(self):
    	return render.admin("Nada")