class Coche:
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

class CocheDeportivo (Coche):
  #Atributos
  marca="Audi"
  modelo="R8"
  puertas="2"
  capacidad="2 personas"
  automatico_o_estandar="estandar"

  #Metodos
  def apagar(self):
    print("apagar")
  def reproducirMusica(self):
    print("reproducir musica")
  def encender(self):
    print("enciende con una llave especial")
  def acelerar(self):
    print("acelera muy rapido")

  def __init__(self):
    print("coche deportivo")
  
OBJETO=Coche()
OBJETO.encender()
OBJETO.acelerar()
print(OBJETO.color)
print(OBJETO.tipo_de_combustible)
print(OBJETO.velocidad_maxima)
print(OBJETO.diseno)
print(OBJETO.tamano)

OBJETO_UN_COCHE = CocheDeportivo()
OBJETO_UN_COCHE.encender()
OBJETO_UN_COCHE.acelerar()
OBJETO_UN_COCHE.apagar()
OBJETO_UN_COCHE.reproducirMusica()
print(OBJETO_UN_COCHE.color)
print(OBJETO_UN_COCHE.tipo_de_combustible)
print(OBJETO_UN_COCHE.velocidad_maxima)
print(OBJETO_UN_COCHE.diseno)
print(OBJETO_UN_COCHE.tamano)
print(OBJETO_UN_COCHE.marca)
print(OBJETO_UN_COCHE.modelo)
print(OBJETO_UN_COCHE.puertas)
print(OBJETO_UN_COCHE.capacidad)
print(OBJETO_UN_COCHE.automatico_o_estandar)
