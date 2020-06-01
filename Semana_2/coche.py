class Coche:
 #Atributos
  color="gris"
  tipo_de_combustible="gasolina"
  velocidad_maxima="300 kilometros"
  diseno="deportivo"
  tamano="chico"
  marca="Audi"
  modelo="R8"
  puertas="2"
  capacidad="2 personas" 
  automatico_o_estandar="automatico"


#Metodos
  def encender (self):
    print ("encender")
  def transporta_pasajeros (self):
    print("transporta_pasajeros")
  def comodidad (self):
    print("comodidad")
  def rapidez (self):
    print ("rapidez")
  def acelerar (self):
    print ("acelerar")

  def __init__(self):
    print ("metodos Coche")


objeto_un_coche= Coche()

objeto_un_coche.encender()
objeto_un_coche.transporta_pasajeros()
objeto_un_coche.comodidad()
objeto_un_coche.rapidez()
objeto_un_coche.acelerar()

print (objeto_un_coche.color)
print (objeto_un_coche.tipo_de_combustible)
print (objeto_un_coche.velocidad_maxima)
print (objeto_un_coche.diseno)
print (objeto_un_coche.tamano)
print (objeto_un_coche.marca)
print (objeto_un_coche.modelo)
print (objeto_un_coche.puertas)
print (objeto_un_coche.capacidad)
print (objeto_un_coche.automatico_o_estandar)