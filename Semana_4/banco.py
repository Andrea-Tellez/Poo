class Banco:

  #Atributos
  nombre="Bancoppel"
  tamano="50 m2"
  logo="el nombre delbanco y una llave invertida"
  eslogan="coppel mejora tu vida"
  diseno="cuadrado"

  #Metodos
  def retirar(self):
    print("Retirar")
  def pagar(self):
    print("pagar")

  def __init__(self):
    print:("metodos banco")


class Bancoppel (Banco):
  #Atributos
  horario="9:00 a 19:30 horas"
  color="amarillo"
  servicios="retiros,prestamos, pagos de servicios "
  direccion="cualquier tienda coppel"
  estacionamiento="planta baja"

  #Metodos
  def retirar(self):
    print("retirar grandes cantidades de dinero")
  def pagar(self):
    print("pagar distintos servicios")
  def cobrar(self):
    print("cobrar becas")
  def depositar(self):
    print("depositar")

  def __init__(self):
    print("Bancoppel")

OBJETO=Banco()
OBJETO.retirar()
OBJETO.pagar()
print(OBJETO.nombre)
print(OBJETO.tamano)
print(OBJETO.logo)
print(OBJETO.eslogan)
print(OBJETO.diseno)

OBJETO_UN_BANCO = Bancoppel()
OBJETO_UN_BANCO.retirar()
OBJETO_UN_BANCO.pagar()
OBJETO_UN_BANCO.cobrar()
OBJETO_UN_BANCO.depositar()
print(OBJETO_UN_BANCO.nombre)
print(OBJETO_UN_BANCO.tamano)
print(OBJETO_UN_BANCO.logo)
print(OBJETO_UN_BANCO.eslogan)
print(OBJETO_UN_BANCO.diseno)
print(OBJETO_UN_BANCO.horario)
print(OBJETO_UN_BANCO.color)
print(OBJETO_UN_BANCO.servicios)
print(OBJETO_UN_BANCO.estacionamiento)
print(OBJETO_UN_BANCO.direccion)