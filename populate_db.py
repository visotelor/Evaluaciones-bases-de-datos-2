from models.asignatura import Asignatura
from models.cargo import Cargo
from model.plantilla import Plantilla
a = Asignatura.create("Bases de datos 2")
asig =  Asignatura.getAll()
c =  Cargo.create("Docente")
c =  Cargo.create("Decano Ingenieria")
cargos =  Cargo.getAll()
pl =  Plantilla.create("Plantilla de prueba")
pl.addPregunta("Nueva pregunta")
