class Avion:
 #Atributos
  tipo_de_combustible="queroseno"
  tamano="grande"
  diseno="depende_el_tipo_de_aerolinea"
  velocidad_maxima="900_kilómetros"
  color="blanco"
  capacidad="40_personas"
  dos_alas="si"
  iluminacion="si"
  pantallas="si"
  modelo="A320"

#Metodos
  def puede_volar (self):
    print ("puede_volar")
  def transporta_pasajeros (self):
    print("transporta_pasajeros")
  def comodidad (self):
    print("comodidad")
  def rapidez (self):
    print ("rapidez")
  def acelerar (self):
    print ("acelerar")

  def __init__(self):
    print ("metodos avion")


objeto_un_avion= Avion()

objeto_un_avion.puede_volar()
objeto_un_avion.transporta_pasajeros()
objeto_un_avion.comodidad()
objeto_un_avion.rapidez()
objeto_un_avion.acelerar()

print (objeto_un_avion.tipo_de_combustible)
print (objeto_un_avion.tamano)
print (objeto_un_avion.diseno)
print (objeto_un_avion.velocidad_maxima)
print (objeto_un_avion.color)
print (objeto_un_avion.capacidad)
print (objeto_un_avion.dos_alas)
print (objeto_un_avion.iluminacion)
print (objeto_un_avion.pantallas)
print (objeto_un_avion.modelo)