from models.categoria import Categoria
import web

render = web.template.render('templates/', base="base")

class ListarCategorias:
    def GET(self):
        categorias = Categoria.getAll()
        return render.listar_categorias (categorias)


class CrearCategoria:

    def GET(self):
    	categorias_existentes = Categoria.getAll()
        return render.crear_categoria(categorias_existentes)                                      

    def POST(self):
        datos_in = web.input()
        nombre = datos_in['nombre']
        categoria_padre = datos_in['categoria_padre']
        c = Categoria.create(nombre, categoria_padre)
        raise web.redirect('/categoria/listar/')
 