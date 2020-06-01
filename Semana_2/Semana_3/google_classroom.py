class googleclassroom:
  #Atributos 
  elataforma_gratuita="si"
  buena_organizacion="si"
  es_de_la_empresa_google="completamente"
  logotipo="pizarron y siluetas de personas"
  disponibilidad_para_distintos_dispositivos="para la mayoria de dispositivos"

  #Metodos
  def dejar_tarea(self):
    print("dejar tarea")
  def comunicacion_a_distancia(self):
    print("comunicacion a distancia")

  def __init__(self):
    print:("metodos google classroom")

class googleclassroomutec (googleclassroom):
  #Atributos
  facil_de_usar="facil de usar"
  almacena_informacion="en drive almacena informacion"
  multiplataforma="multiplataforma"
  proporciona_un_codigo_para_las_clases="si para mayor organizacion"
  ensenar="si mediante varios medios"

  #Metodos
  def clases_online(self):
    print("clases online")
  def entregar_trabajos_y_tareas(self):
    print("entregar trabajos y tareas")

  def __init__(self):
    print("Estudiante Andrea")

objeto=googleclassroom()
objeto.dejar_tarea()
objeto.comunicacion_a_distancia()
print(objeto.plataforma_gratuita)
print(objeto.buena_organizacion)
print(objeto.es_de_la_empresa_google)
print(objeto.logotipo)
print(objeto.disponibilidad_para_distintos_dispositivos)


objeto_una_app = googleclassroomutec()
objeto_una_app.dejar_tarea()
objeto_una_app.comunicacion_a_distancia()
objeto_una_app.clases_online()
objeto_una_app.entregar_trabajos_y_tareas()
print(objeto_una_app.plataforma_gratuita)
print(objeto_una_app.buena_organizacion)
print(objeto_una_app.es_de_la_empresa_google)
print(objeto_una_app.logotipo)
print(objeto_una_app.disponibilidad_para_distintos_dispositivos)
print(objeto_una_app.facil_de_usar)
print(objeto_una_app.almacena_informacion)
print(objeto_una_app.multiplataforma)
print(objeto_una_app.proporciona_un_codigo_para_las_clases)
print(objeto_una_app.ensenar)
