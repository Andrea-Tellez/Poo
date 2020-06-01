class Google_classroom:
  #ATRIBUTOS
  plataforma_gratuita="completamente"
  buena_organizacion="si"
  es_de_la_empresa_google="completamente"
  tiene_un_logotipo="pizarron y siluetas de personas"
  disponibilidad_para_distintos_dispositivos="para la mayoria de dispositivos"
  facil_de_usar="si"
  almacena_informacion="si en drive"
  multiplataforma="si"
  proporciona_un_codigo_para_las_clases="si"
  ensenar="si"

  #METODOS
  def dejar_tarea(self):
    print("dejar tarea")
  def comunicacion_a_distancia(self):
    print("comunicacion a distancia")
  def clases_online(self):
    print("clases online")
  def entregar_trabajos_y_tareas(self):
    print("entregar trabajos y tareas")
  def crear_documentos(self):
    print("crear documentos")
  
  def __init__(self):
    print("metodos Google_classroom")


objeto_una_app = Google_classroom()

objeto_una_app.dejar_tarea()
objeto_una_app.comunicacion_a_distancia()
objeto_una_app.clases_online()
objeto_una_app.entregar_trabajos_y_tareas()
objeto_una_app.crear_documentos()

print(objeto_una_app.plataforma_gratuita)
print(objeto_una_app.buena_organizacion)
print(objeto_una_app.es_de_la_empresa_google)
print(objeto_una_app.tiene_un_logotipo)
print(objeto_una_app.disponibilidad_para_distintos_dispositivos)
print(objeto_una_app.facil_de_usar)
print(objeto_una_app.almacena_informacion)
print(objeto_una_app.multiplataforma)
print(objeto_una_app.proporciona_un_codigo_para_las_clases)
print(objeto_una_app.ensenar)