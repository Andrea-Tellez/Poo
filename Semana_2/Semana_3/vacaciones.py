class Vacaciones:
  #Atributos 
  irrenunciable="es un derecho en el trabajo"
  Duracion="1 semana"
  viajar_o_realizar_un_recorrido="si"
  realizar_gastos="si"
  descansar_de_una_actividad_habitual="si"

  #Metodos
  def distraccion(self):
    print("distraccion")
  def diversion(self):
    print("diversion")

  def __init__(self):
    print:("metodos vacaciones")

class Vacacionescancun (Vacaciones):
  #Atributos
  esta_relacionado_con_el_turismo="si"
  uso_de_maletas="si"
  fechas_establecidas="1_de_junio_al_8_de_junio"
  conocimiento_de_diversidad="si"
  salir_de_casa="si"

  #Metodos
  def entretenimiento(self):
    print("entretenimiento")
  def comprar_recuerdos(self):
    print("comprar recuerdos")

  def __init__(self):
    print("vacaciones cancun")

objeto=Vacaciones()
objeto.distraccion()
objeto.diversion()
print(objeto.irrenunciable)
print(objeto.duracion)
print(objeto.viajar_o_realizar_un_recorrido)
print(objeto.realizar_gastos)
print(objeto.descansar_de_una_actividad_habitual)



objeto_unas_vacaciones = Vacacionescancun()
objeto_unas_vacaciones.distraccion()
objeto_unas_vacaciones.diversion()
objeto_unas_vacaciones.entretenimiento()
objeto_unas_vacaciones.comprar_recuerdos()
print(objeto_unas_vacaciones.irrenunciable)
print(objeto_unas_vacaciones.duracion)
print(objeto_unas_vacaciones.viajar_o_realizar_un_recorrido)
print(objeto_unas_vacaciones.realizar_gastos)
print(objeto_unas_vacaciones.descansar_de_una_actividad_habitual)
print(objeto_unas_vacaciones.esta_relacionado_con_el_turismo)
print(objeto_unas_vacaciones.uso_de_maletas)
print(objeto_unas_vacaciones.fechas_establecidas)
print(objeto_unas_vacaciones.conocimiento_de_diversidad)
print(objeto_unas_vacaciones.salir_de_casa)
