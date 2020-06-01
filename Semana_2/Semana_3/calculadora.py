class calculadora:
  #Atributos 
  aparato_portatil="si"
  tamano="chica"
  diseno="colorido"
  aparato_electronico="si es un aparato electronico"
  tiene_numeros="si tiene numeros"

  #Metodos
  def realizar_calculos(self):
    print("realizar calculos")
  def encender(self):
    print("encender")

  def __init__(self):
    print:("metodos calculadora")

class calculadoraportatil (calculadora):
  #Atributos
  color="rosa"
  numeros="del 0 al 9"
  signos_matematicos="si tiene signos matematicos"
  las_operaciones_aritmeticas="si las 4 operaciones basicas"
  el_signo_igual="si"

  #Metodos
  def boton_para_cancelar(self):
    print("boton para cancelar")
  def muestra_resultados(self):
    print("muestra resultados")

  def __init__(self):
    print("calculadora portatil")

objeto=calculadora()
objeto.realizar_calculos()
objeto.encender()
print(objeto.aparato_portatil)
print(objeto.tamano)
print(objeto.diseno)
print(objeto.aparato_electronico)
print(objeto.tiene_numeros)



objeto_una_calculadora = calculadoraportatil()
objeto_una_calculadora.realizar_calculos()
objeto_una_calculadora.encender()
objeto_una_calculadora.boton_para_cancelar()
objeto_una_calculadora.muestra_resultados()
print(objeto_una_calculadora.aparato_portatil)
print(objeto_una_calculadora.tamano)
print(objeto_una_calculadora.diseno)
print(objeto_una_calculadora.aparato_electronico)
print(objeto_una_calculadora.tiene_numeros)
print(objeto_una_calculadora.color)
print(objeto_una_calculadora.numeros)
print(objeto_una_calculadora.signos_matematicos)
print(objeto_una_calculadora.las_operaciones_aritmeticas)
print(objeto_una_calculadora.el_signo_igual
