class Banco:

  #Atributos
  nombre="Bancoppel"
  tamano="50 m2"
  logo="el nombre delbanco y una llave invertida"
  eslogan="coppel mejora tu vida"
  diseno="cuadrado"
  horario="9:00 a 19:30 horas"
  color="amarillo"
  servicios="retiros,prestamos, pagos de servicios "
  direccion="cualquier tienda coppel"
  estacionamiento="planta baja"

  #Metodos
  def retirar_dinero (self):
    print ("Retirar dinero")
  def depositar (self):
    print("depositar")
  def hacer_prestamos (self):
    print("hacer prestamos")
  def pagar (self):
    print ("pagar")
  def cobrar (self):
    print ("cobrar")

  def __init__(self):
    print ("metodos banco")


objeto_un_banco= Banco()

objeto_un_banco.retirar_dinero()
objeto_un_banco.depositar()
objeto_un_banco.hacer_prestamos()
objeto_un_banco.pagar()
objeto_un_banco.cobrar()


print (objeto_un_banco.nombre)
print (objeto_un_banco.tamano)
print (objeto_un_banco.logo)
print (objeto_un_banco.eslogan)
print (objeto_un_banco.diseno)
print (objeto_un_banco.horario)
print (objeto_un_banco.color)
print (objeto_un_banco.servicios)
print (objeto_un_banco.direccion)
print (objeto_un_banco.estacionamiento)