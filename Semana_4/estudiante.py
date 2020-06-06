class Estudiante:
  #Atributos 
  nombre= "Andrea"
  matricula= "17191101"
  carrera= "tic´s"
  edad= "18"
  cuatrimestre= "segundo"

  #Metodos
  def elegir(self):
    print("elegir")
  def asignar(self):
    print("asignar")

  def __init__(self):
    print:("metodos estudiante")

class EstudianteAndrea (Estudiante):
  #Atributos
  promedio=("9.6")
  beca="ninguna"
  tutor="oscar"
  grupo="22"
  nivel_de_ingles="A2"

  #Metodos
  def tareas(self):
    print("tareas")
  def pasar(self):
    print("pasar")
  def elegir(self):
    print("elegir carrera ")
  def asignar(self):
    print("asignar tareas")

  def __init__(self):
    print("Estudiante Andrea")
objeto=Estudiante()
objeto.elegir()
objeto.asignar()
print(objeto.nombre)
print(objeto.matricula)
print(objeto.carrera)
print(objeto.edad)
print(objeto.cuatrimestre)

OBJETO=Estudiante()
OBJETO.elegir()
OBJETO.asignar()
print(OBJETO.nombre)
print(OBJETO.matricula)
print(OBJETO.carrera)
print(OBJETO.edad)
print(OBJETO.cuatrimestre)

OBJETO_ESTUDIANTE_ANDREA=EstudianteAndrea()
OBJETO_ESTUDIANTE_ANDREA.elegir()
OBJETO_ESTUDIANTE_ANDREA.asignar()
OBJETO_ESTUDIANTE_ANDREA.tareas()
OBJETO_ESTUDIANTE_ANDREA.pasar()
print(OBJETO_ESTUDIANTE_ANDREA.nombre)
print(OBJETO_ESTUDIANTE_ANDREA.matricula)
print(OBJETO_ESTUDIANTE_ANDREA.carrera)
print(OBJETO_ESTUDIANTE_ANDREA.edad)
print(OBJETO_ESTUDIANTE_ANDREA.cuatrimestre)
print(OBJETO_ESTUDIANTE_ANDREA.promedio)
print(OBJETO_ESTUDIANTE_ANDREA.beca)
print(OBJETO_ESTUDIANTE_ANDREA.tutor)
print(OBJETO_ESTUDIANTE_ANDREA.grupo)
print(OBJETO_ESTUDIANTE_ANDREA.nivel_de_ingles)
