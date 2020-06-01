class Banco:
  #Atributos 
  nombre="Bancoppel"
  tamano="50 m2"
  logo="una llave invertida"
  eslogan="coppel mejora tu vida"
  diseno="cuatrado"

  #Metodos
  def retirar(self):
    print("retirar")
  def pagar(self):
    print("pagar")

  def __init__(self):
    print:("metodos banco")

class Bancoppel (Banco):
  #Atributos
  horario="9:00a.m-19:30p.m"
  color="amarillo"
  servicios="depositos.retiros.pretamos"
  cajeros="3"
  estacionamiento="en la planta baja"

  #Metodos
  def cobrar(self):
    print("cobrar")
  def depositar(self):
    print("depositar")

  def __init__(self):
    print("Bancoppel")

objeto=Banco()
objeto.retirar()
objeto.pagar()
print(objeto.nombre)
print(objeto.tamano)
print(objeto.logo)
print(objeto.eslogan)
print(objeto.diseno)



objeto_un_banco = Bancoppel()
objeto_un_banco.retirar()
objeto_un_banco.pagar()
objeto_un_banco.cobrar()
objeto_un_banco.depositar()
print(objeto_un_banco.nombre)
print(objeto_un_banco.tamano)
print(objeto_un_banco.logo)
print(objeto_un_banco.eslogan)
print(objeto_un_banco.diseno)
print(objeto_un_banco.horario)
print(objeto_un_banco.color)
print(objeto_un_banco.servicios)
print(objeto_un_banco.cajeros)
print(objeto_un_banco.estacionamiento)
