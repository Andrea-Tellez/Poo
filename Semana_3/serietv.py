class serieTV:
  #Atributos 
  es_transmitida_en_dispositivos_tecnologicos="si"
  es_dirigida_a_un_publico_especifico="si"
  tiene_una_duracion="si"
  es_una_obra_audiovisual="si"
  tiene_episodios="si"

  #Metodos
  def entretenimiento(self):
    print("entretenimiento")
  def enrriquecimiento_de_conocimientos(self):
    print("enrriquecimiento de conocimientos")

  def __init__(self):
    print:("metodos serieTV")

class serietvamazon(serieTV):
  #Atributos
  tiene_una_Tematica="amor."
  horario_de_transmision="4pm"
  cuenta_con_un_presupuesto="si"
  tiene_un_objetivo="si"
  calidad="hd"

  #Metodos
  def diversion(self):
    print("diversion")
  def desata_emociones(self):
    print("desata emociones")

  def __init__(self):
    print("serie de amazon")

objeto=serieTV()
objeto.entretenimiento()
objeto.enrriquecimiento_de_conocimientos()
print(objeto.es_transmitida_en_dispositivos_tecnologicos)
print(objeto.es_dirigida_a_un_publico_especifico)
print(objeto.tiene_una_duracion)
print(objeto.es_una_obra_audiovisual)
print(objeto.tiene_episodios)

objeto_una_serie = serietvamazon()
objeto_una_serie.entretenimiento()
objeto_una_serie.enrriquecimiento_de_conocimientos()
objeto_una_serie.diversion()
objeto_una_serie.desata_emociones()
print(objeto_una_serie.es_transmitida_en_dispositivos_tecnologicos)
print(objeto_una_serie.es_dirigida_a_un_publico_especifico)
print(objeto_una_serie.tiene_una_duracion)
print(objeto_una_serie.es_una_obra_audiovisual)
print(objeto_una_serie.tiene_episodios)
print(objeto_una_serie.tiene_una_Tematica)
print(objeto_una_serie.horario_de_transmision)
print(objeto_una_serie.cuenta_con_un_presupuesto)
print(objeto_una_serie.tiene_un_objetivo)
print(objeto_una_serie.calidad)