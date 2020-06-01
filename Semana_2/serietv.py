class Serietv:

  #Atributos
  es_transmitida_en_dispositivos_tecnologicos= "si"
  es_dirigida_a_un_publico_especifico="si"
  calidad="buena"
  duracion="40_minutos"
  es_una_obra_audiovisual="si"
  episodios="12_episodios"
  tematica="amor"
  horario_de_transmision="5_pm"
  cuenta_con_un_presupuesto="si"
  tiene_un_objetivo="si"

  #Metodos
  def entretenimiento (self):
    print ("entretenimiento")
  def enriquecimiento_de_conocimiento (self):
    print("enriquecimiento_deconocimiento")
  def distraccion (self):
    print("distraccion")
  def diversion (self):
    print ("diversion")
  def desata_emociones (self):
    print ("desata_emociones")

  def __init__(self):
    print ("metodos serietv")


objeto_una_serietv= Serietv()

objeto_una_serietv.entretenimiento()
objeto_una_serietv.enriquecimiento_de_conocimiento()
objeto_una_serietv.distraccion()
objeto_una_serietv.diversion()
objeto_una_serietv.desata_emociones()


print (objeto_una_serietv.es_transmitida_en_dispositivos_tecnologicos)
print (objeto_una_serietv.es_dirigida_a_un_publico_especifico)
print (objeto_una_serietv.calidad)
print (objeto_una_serietv.duracion)
print (objeto_una_serietv.es_una_obra_audiovisual)
print (objeto_una_serietv.episodios)
print (objeto_una_serietv.tematica)
print (objeto_una_serietv.horario_de_transmision)
print (objeto_una_serietv.cuenta_con_un_presupuesto)
print (objeto_una_serietv.tiene_un_objetivo)
