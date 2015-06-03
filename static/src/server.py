#Importo modulo de conexion con DB y web server
import web 
import json
import fdb
import datetime
con = fdb.connect(dsn='localhost:/opt/firebird/data/agenda.gdb', user='sysdba', password='clave')
        

urls = (
    '/', 'mostrar_citas',
    '/crear_cita/.*', 'crear_cita',
)

class crear_cita:
    def GET(self):
        crear_cita_template = web.template.frender('crear_cita.html')
        return crear_cita_template(mensaje = "nada")
    def POST(self):
        #fecha = datetime("")
        #Revisa si existe fecha
        datos_in = web.input()
        fecha = datos_in['fecha']
        prioridad = datos_in['prioridad']
        hora = datos_in['hora']
        duracion = datos_in['duracion']
        descripcion = datos_in['descripcion']
        try:
            q = "SELECT id_fecha FROM fechas WHERE fecha = CAST ('%s' as date)" % (fecha)
            cur1 = con.cursor()
            cur1.execute(q)
            id_fecha = cur1.fetchone()[0]
            print id_fecha
            cur1.close()
            fecha_creada = False
            #Crea fecha
        except:
            q = "INSERT INTO fechas (fecha) values ('"+fecha+"') RETURNING id_fecha;"
            print q
            cur1 = con.cursor()
            cur1.execute(q)
            id_fecha = cur1.fetchone()[0]
            con.commit()
            fecha_creada = True
        try: 
            q = "INSERT INTO citas (prioridad, duracion, hora, id_fecha, descripcion) VALUES (%s, %s, '%s', '%s', '%s')" % (prioridad, duracion, str(hora), id_fecha, descripcion)
            print q
            cur1 = con.cursor()
            mensaje = "Cita creada"
            cur1.execute(q)
            con.commit()
            if fecha_creada:
                mensaje += " \n, es la primera cita en esa fecha"
            else:
                mensaje += " \n La fecha tambien fue creada"
        except:
            mensaje = "Revise por favor los paremetros de entrada, recuerde que la cita debe estar programada entre 8:00 y 19:00"

  
        #Si no esta crea una una nueva cita
        crear_cita_template = web.template.frender('crear_cita.html')
        return crear_cita_template(mensaje = mensaje)


class mostrar_citas():
    def GET(self):
        q = "SELECT fechas.fecha, citas.hora, citas.duracion, citas.prioridad, citas.descripcion FROM fechas, citas WHERE citas.id_fecha=fechas.id_fecha"
        print q
        cur1 = con.cursor()
        cur1.execute(q)
        datos = list(cur1.fetchall())
        cur1.close()
        mostrar_cita_template = web.template.frender('index.html')
        return mostrar_cita_template(datos = datos)
    def POST(self):
        #http://www.w3resource.com/sql/joins/using-a-where-cluase-to-join-two-tables-related-by-a-single-column-primary-key-or-foriegn-key-pair.php
        fecha = web.input()['fecha']
        q =  "SELECT ID_FECHA FROM FECHAS WHERE FECHA = CAST ('%s' as date)" % fecha ;
        print q
        cur2 = con.cursor()
        cur2.execute(q)
        id_fecha = cur2.fetchone()[0]
        cur2.close()
        q = "SELECT f.fecha, c.hora, c.duracion, c.prioridad, c.descripcion FROM fechas f, citas c WHERE c.id_fecha=%s AND f.id_fecha=%s"  % (id_fecha, id_fecha) ;
        print q
        cur1 = con.cursor()
        cur1.execute(q)
        datos = list(cur1.fetchall())
        cur1.close()
        mostrar_cita_template = web.template.frender('index.html')
        return mostrar_cita_template(datos = datos)


    #Recibe fecha de REST
    #Despliega resultado


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()


