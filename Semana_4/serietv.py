class SerieTV:
  #Atributos 
  es_transmitida_en_dispositivos_tecnologicos="si"
  es_dirigida_a_un_publico_especifico="si"
  tiene_una_duracion="si"
  es_una_obra_audiovisual="si"
  tiene_episodios="si"

  #Metodos
  def entretenimiento(self):
    print("entretenimiento")
  def enrriquecimientodeConocimientos(self):
    print("enrriquecimiento de conocimientos")

  def __init__(self):
    print:("metodos serieTV")

class SerietvAmazon(SerieTV):
  #Atributos
  tiene_una_tematica="amor."
  horario_de_transmision="4pm"
  cuenta_con_un_presupuesto="si"
  tiene_un_objetivo="si"
  calidad="hd"

  #Metodos
  def diversion(self):
    print("diversion")
  def desataEmociones(self):
    print("desata emociones")
  def entretenimiento(self):
    print("entretenimiento durante un periodo")
  def enrriquecimientodeConocimientos(self):
    print("enrriquecimiento de conocimientos si se trata de algun documental")


  def __init__(self):
    print("serie de amazon")



OBJETO=SerieTV()
OBJETO.entretenimiento()
OBJETO.enrriquecimientodeConocimientos()
print(OBJETO.es_transmitida_en_dispositivos_tecnologicos)
print(OBJETO.es_dirigida_a_un_publico_especifico)
print(OBJETO.tiene_una_duracion)
print(OBJETO.es_una_obra_audiovisual)
print(OBJETO.tiene_episodios)

OBJETO_UNA_SERIE = SerietvAmazon()
OBJETO_UNA_SERIE.entretenimiento()
OBJETO_UNA_SERIE.enrriquecimientodeConocimientos()
OBJETO_UNA_SERIE.diversion()
OBJETO_UNA_SERIE.desataEmociones()
print(OBJETO_UNA_SERIE.es_transmitida_en_dispositivos_tecnologicos)
print(OBJETO_UNA_SERIE.es_dirigida_a_un_publico_especifico)
print(OBJETO_UNA_SERIE.tiene_una_duracion)
print(OBJETO_UNA_SERIE.es_una_obra_audiovisual)
print(OBJETO_UNA_SERIE.tiene_episodios)
print(OBJETO_UNA_SERIE.tiene_una_tematica)
print(OBJETO_UNA_SERIE.horario_de_transmision)
print(OBJETO_UNA_SERIE.cuenta_con_un_presupuesto)
print(OBJETO_UNA_SERIE.tiene_un_objetivo)
print(OBJETO_UNA_SERIE.calidad)
