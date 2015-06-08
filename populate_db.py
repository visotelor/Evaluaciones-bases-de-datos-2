from models.asignatura import Asignatura
from models.cargo import Cargo
from models.plantilla import Plantilla
from models.usuario import Usuario, Administrador, Estudiante, Estructura, Funcionario
from models.tesis import Tesis

#Creo 2 asignaturas
a1 = Asignatura.create("Bases de datos 2")
a2 = Asignatura.create("Bases de datos 1")

# Creo algunos cargos
docente_c =  Cargo.create("Docente")
decano_ing_c = Cargo.create("Decano Ingenieria")
rector_c = Cargo.create("Rector") 
coordinador_ing_sistemas = Cargo.create("Coordinador ingenieria de sistemas")

#Creo una plantilla y anado una pregunta
pl = Plantilla.create("Plantilla de prueba")
pl.addPregunta("Nueva pregunta")

#Creo usuario administrador
u1 = Usuario.create("Cristian Rojas", "carojasq", "contrasena", "carojasq@u.co")
a1 = Administrador.create(u1)

#Creo una estructura (rectoria)
u1 = Usuario.create("Rectoria",  "rectoria", "contrasena", "recotoria@u.co")
es1 = Estructura.create(u1, rector_c)

#Creo una estructura derivada de rectoria
u2 = Usuario.create("Decanatura de ingenieria",  "decanaturaing", "contrasena", "decanaturaing@u.co")
es2 = Estructura.create(u2, decano_ing_c, es1)

#Creo proyecto curricular, derivado de decanatura
u3 = Usuario.create("Ingenieria de sistemas",  "ingsistemas", "contrasena", "ingsistemas@u.co")
es3 = Estructura.create(u3, coordinador_ing_sistemas, es2)


#Creo un estudiante
u10 =  Usuario.create("Fabian Puentes", "fpuentes", "contrasena", "fpuentes@u.co")
e10 = Estudiante.create(u10, "54535453", es3)

#Creo un funcionario y le doy cargo
u11 = Usuario.create("Sonia Ordonez", "soniaordo", "contrasena", "soniaordo@u.co")
f11 = Funcionario.create(u11, "8789798")
f11.setCargo(docente_c)

#Creo una tesis
t1 = Tesis.create("Este es el titulo")

#Doy tesis a estudiante
e10.setTesis(t1)

#Ejemplo para obtener el tipo de un usuario
tipo = u11.getTipo(u11.id)




