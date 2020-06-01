class Calculadora:

  #Atributos
  aparato_portatil_o_de_escritorio="si"
  aparato_electronico="si"
  existen_calculadoras_graficas="si"
  tamano="pequeño"
  diseno="cuadrado"
  operaciones_aritmeticas="suma_resta_multiplicacion_division"
  color="gris"
  tiene_numeros="si"
  marca="casio"
  el_signo_igual_para_obtener_el_resultado="si"


  #Metodos
  def encender (self):
    print ("encender")
  def realiza_calculos (self):
    print("realiza_calculos")
  def muestra_un_resultado (self):
    print("muestra_un_resultado")
  def apagar (self):
    print ("apagar")
  def boton_para_cancelar_una_operacion_en_curso (self):
    print ("boton_para_cancelar_una_operacion_en_curso")

  def __init__(self):
    print ("metodos Calculadora")


objeto_una_calculadora= Calculadora()

objeto_una_calculadora.encender()
objeto_una_calculadora.realiza_calculos()
objeto_una_calculadora.muestra_un_resultado()
objeto_una_calculadora.apagar()
objeto_una_calculadora.boton_para_cancelar_una_operacion_en_curso()


print(objeto_una_calculadora.aparato_portatil_o_de_escritorio)
print (objeto_una_calculadora.aparato_electronico)
print (objeto_una_calculadora.existen_calculadoras_graficas)
print (objeto_una_calculadora.tamano)
print (objeto_una_calculadora.diseno)
print (objeto_una_calculadora.operaciones_aritmeticas)
print (objeto_una_calculadora.color)
print (objeto_una_calculadora.tiene_numeros)
print (objeto_una_calculadora.marca)
print (objeto_una_calculadora.el_signo_igual_para_obtener_el_resultado)