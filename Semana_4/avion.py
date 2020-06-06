class Avion:
  #Atributos 
  tipo_de_combustible="queroseno"
  tamano="grande"
  diseno="depende_del_tipo_de_aerolinea"
  velocida_maxima="900km/hra"
  color="blanco"

  #Metodos
  def puedeVolar(self):
    print("puede volar")
  def transportaPasajeros(self):
    print("trasporta pasajeros")

  def __init__(self):
    print:("metodos avion")

class AvionYet (Avion):
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
  def puedeVolar(self):
    print("a altas alturas ")
  def transportaPasajeros(self):
    print("trasporta niños, jovenes y abuelos ")


  def __init__(self):
    print("Avion Yet")

OBJETO=Avion()
OBJETO.puedeVolar()
OBJETO.transportaPasajeros()
print(OBJETO.tipo_de_combustible)
print(OBJETO.tamano)
print(OBJETO.diseno)
print(OBJETO.velocida_maxima)
print(OBJETO.color)

OBJETO_UN_AVION = AvionYet()
OBJETO_UN_AVION.puedeVolar()
OBJETO_UN_AVION.transportaPasajeros()
OBJETO_UN_AVION.comodidad()
OBJETO_UN_AVION.rapidez()
print(OBJETO_UN_AVION.tipo_de_combustible)
print(OBJETO_UN_AVION.tamano)
print(OBJETO_UN_AVION.diseno)
print(OBJETO_UN_AVION.velocida_maxima)
print(OBJETO_UN_AVION.color)
print(OBJETO_UN_AVION.capacidad)
print(OBJETO_UN_AVION.dos_alas)
print(OBJETO_UN_AVION.iluminacion)
print(OBJETO_UN_AVION.banos)
print(OBJETO_UN_AVION.tienen_pantallas)


