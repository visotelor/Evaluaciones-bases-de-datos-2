from models.usuario import Usuario
from models.administrador import Administrador
#from models.despachador import Despachador
#from models.usuario_de_internet import Usuario_de_internet
#from models.ciudad import Ciudad
import web


render = web.template.render('templates/', base="base")

class ListarUsuarios:
    def GET(self):
        datos = {}
        datos['administradores'] = Administrador.getAll()
        datos['despachadores'] = Despachador.getAll()
        datos['usuarios'] = Usuario_de_internet.getAll()
        return render.listar_usuarios (datos)


class CrearUsuario:

    def GET(self):
    	datos = {}
        datos['ciudades'] = Ciudad.getAll()
        return render.crear_usuario(datos) 

    def POST(self):
        datos_in = web.input()
        nombre_completo = datos_in['nombre_completo']
        identificacion = datos_in['identificacion']
        e_mail = datos_in['e_mail']
        usuario = datos_in ['usuario']
        contrasena= datos_in['contrasena']
        direccion_residencia = datos_in['direccion_residencia']
        ciudad_residencia = datos_in['ciudad_residencia']
        sexo = datos_in['sexo']
        fecha_nacimiento= datos_in['fecha']
        telefono =   datos_in['telefono']
        direccion_despacho = datos_in['direccion_despacho']
        ciudad_despacho = datos_in['ciudad_despacho']
        user = Usuario.create(identificacion,nombre_completo, usuario, contrasena, e_mail,direccion_residencia,ciudad_residencia)
        if "Usuario_de_internet" in datos_in:
            Usuario_de_internet.create(identificacion,sexo, fecha_nacimiento, direccion_despacho, ciudad_despacho, telefono)
        if "Administrador" in datos_in:
            Administrador.create(identificacion)
        if "Despachador" in datos_in:
            Despachador.create(identificacion)
        raise web.redirect('/usuario/listar/')

 