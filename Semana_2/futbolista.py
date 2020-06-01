class futbolista:
  #ATRIBUTOS
  usa_uniforme="si"
  juega_en_una_chancha_de_futbol="si"
  velocidad="rapida"
  fuerza="mucha"
  agilidad="si"
  motivacion="si"
  flexibilidad="si"
  coordinacion="si"
  calzado_especial="tacos"
  diciplina="si"

  #METODOS
  def funcion_o_posicion(self):
    print("funcion o posicion")
  def juega_un_deporte_especifico(self):
    print("juega un deporte especifico")
  def dominar_el_oponente(self):
    print("domina al oponente")
  def habilidad(self):
    print("habilidad")
  def meter_goles(self):
    print("meter goles")
  
  def __init__(self):
    print("metodos futbolista")


objeto_un_futbolista = futbolista()

objeto_un_futbolista.funcion_o_posicion()
objeto_un_futbolista.juega_un_deporte_especifico()
objeto_un_futbolista.dominar_el_oponente()
objeto_un_futbolista.habilidad()
objeto_un_futbolista.meter_goles()

print(objeto_un_futbolista.usa_uniforme)
print(objeto_un_futbolista.juega_en_una_chancha_de_futbol)
print(objeto_un_futbolista.velocidad)
print(objeto_un_futbolista.fuerza)
print(objeto_un_futbolista.agilidad)
print(objeto_un_futbolista.motivacion)
print(objeto_un_futbolista.flexibilidad)
print(objeto_un_futbolista.coordinacion)
print(objeto_un_futbolista.calzado_especial)
print(objeto_un_futbolista.diciplina)