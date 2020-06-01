
class coche:
  #Atributos 
  color="gris"
  tipo_de_combustible="gasolina"
  velocidad_maxima="331 kh/h "
  diseno="deportivo"
  tamano="estandar"

  #Metodos
  def encender(self):
    print("encender")
  def acelerar(self):
    print("acelerar")

  def __init__(self):
    print:("metodos coche")

class cochedeportivo (coche):
  #Atributos
  Marca="Audi"
  Modelo="R8"
  puertas="2"
  Capacidad="2 personas"
  Automatico_o_Estandar="estandar"

  #Metodos
  def apagar(self):
    print("apagar")
  def reproducir_musica(self):
    print("reproducir musica")

  def __init__(self):
    print("coche deportivo")

objeto=coche()
objeto.encender()
objeto.acelerar()
print(objeto.color)
print(objeto.tipo_de_combustible)
print(objeto.velocidad_maxima)
print(objeto.diseno)
print(objeto.tamano)

objeto_un_coche = cochedeportivo()
objeto_un_coche.encender()
objeto_un_coche.acelerar()
objeto_un_coche.apagar()
objeto_un_coche.reproducir_musica()
print(objeto_un_coche.color)
print(objeto_un_coche.tipo_de_combustible)
print(objeto_un_coche.velocidad_maxima)
print(objeto_un_coche.diseno)
print(objeto_un_coche.tamano)
print(objeto_un_coche.marca)
print(objeto_un_coche.modelo)
print(objeto_un_coche.puertas)
print(objeto_un_coche.capacidad)
print(objeto_un_coche.automatico_o_Estandar)
