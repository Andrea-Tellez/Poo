class Avion:
  #Atributos 
  tipo_de_combustible="queroseno"
  tamano="grande"
  diseno="depende_del_tipo_de_aerolinea"
  velocida_maxima="900km/hra"
  color="blanco"

  #Metodos
  def puede_volar(self):
    print("puede volar")
  def transporta_pasajeros(self):
    print("trasporta pasajeros")

  def __init__(self):
    print:("metodos avion")

class avionyet (Avion):
  #Atributos
  capacidad="250"
  dos_alas="si"
  iluminacion="si"
  banos="si"
  tienen_pantallas="si"

  #Metodos
  def comodidad(self):
    print("comodidad")
  def rapidez(self):
    print("rapidez")

  def __init__(self):
    print("Avion Yet")

objeto=Avion()
objeto.puede_volar()
objeto.transporta_pasajeros()
print(objeto.tipo_de_combustible)
print(objeto.tamano)
print(objeto.diseno)
print(objeto.velocida_maxima)
print(objeto.color)



objeto_un_avion = avionyet()
objeto_un_avion.puede_volar()
objeto_un_avion.transporta_pasajeros()
objeto_un_avion.comodidad()
objeto_un_avion.rapidez()
print(objeto_un_avion.tipo_de_combustible)
print(objeto_un_avion.tamano)
print(objeto_un_avion.diseno)
print(objeto_un_avion.velocida_maxima)
print(objeto_un_avion.color)
print(objeto_un_avion.capacidad)
print(objeto_un_avion.dos_alas)
print(objeto_un_avion.iluminacion)
print(objeto_un_avion.banos)
print(objeto_un_avion.tienen_pantallas)