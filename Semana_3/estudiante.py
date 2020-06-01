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

objeto_estudiante_Andrea=EstudianteAndrea()
objeto_estudiante_Andrea.tareas()
objeto_estudiante_Andrea.pasar()
objeto_estudiante_Andrea.elegir()
objeto_estudiante_Andrea.asignar()
print(objeto_estudiante_Andrea.nombre)
print(objeto_estudiante_Andrea.matricula)
print(objeto_estudiante_Andrea.carrera)
print(objeto_estudiante_Andrea.edad)
print(objeto_estudiante_Andrea.cuatrimestre)
print(objeto_estudiante_Andrea.promedio)
print(objeto_estudiante_Andrea.beca)
print(objeto_estudiante_Andrea.tutor)
print(objeto_estudiante_Andrea.grupo)
print(objeto_estudiante_Andrea.nivel_de_ingles)