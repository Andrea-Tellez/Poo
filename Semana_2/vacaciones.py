class vacaciones:
 #Atributos
  irrenunciable="si"
  duracion="2_semanas"
  realizar_un_recorrido="si"
  realizar_un_gasto="si"
  descansar_de_una_actividad_habitual="si"
  esta_relacionado_con_el_turismo="si"
  uso_de_maletas="si"
  fechas_establecidas="12_de_mayo_al_26_de_mayo"
  conocimiento_de_diversidad="si"
  salir_de_casa="si"


#Metodos
  def distraccion (self):
    print ("distraccion")
  def diversion (self):
    print("diversion")
  def entretenimiento (self):
    print("entretenimiento")
  def comprar_recuerdos (self):
    print ("comprar_recuerdos")
  def tomar_fotografias (self):
    print ("tomar_fotografias")

  def __init__(self):
    print ("metodos vacaciones")


objeto_unas_vacaciones= vacaciones()

objeto_unas_vacaciones.distraccion()
objeto_unas_vacaciones.diversion()
objeto_unas_vacaciones.entretenimiento()
objeto_unas_vacaciones.comprar_recuerdos()
objeto_unas_vacaciones.tomar_fotografias()

print (objeto_unas_vacaciones.irrenunciable)
print (objeto_unas_vacaciones.duracion)
print (objeto_unas_vacaciones.realizar_un_recorrido)
print (objeto_unas_vacaciones.realizar_un_gasto)
print(objeto_unas_vacaciones.descansar_de_una_actividad_habitual)
print (objeto_unas_vacaciones.esta_relacionado_con_el_turismo)
print (objeto_unas_vacaciones.uso_de_maletas)
print (objeto_unas_vacaciones.fechas_establecidas)
print (objeto_unas_vacaciones.conocimiento_de_diversidad)
print (objeto_unas_vacaciones.salir_de_casa)