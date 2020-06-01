class cajeroautomatico:
  #Atributos 
  disponibilidad="las 24 horas"
  escaner_para_reconocer_tarjetas="si escanea tarjetas"
  teclado_numerico="tiene teclado numerico"
  pantallas_touch="la mayoria"
  una_computadora="si tiene una computadora"

  #Metodos
  def retirar_dinero(self):
    print("retirar dinero")
  def consultar_tu_saldo(self):
    print("consultar tu saldo")

  def __init__(self):
    print:("metodos cajero automatico")

class cajeroautomaticoBancomer (cajeroautomatico):
  #Atributos
  tamano="estandar"
  color="depende el banco"
  diseno="estandar"
  lo_ofrece_una_institucion_bancaria="lo ofrece bancomer"
  imprime_comprobantes="imprime comprobantes"

  #Metodos
  def realizar_pagos_de_servicios(self):
    print("realizar pagos de servicios")
  def reconocer_y_validar_billetes(self):
    print("reconocer y validar billetes")

  def __init__(self):
    print("cajero automatico bancomer")

objeto=cajeroautomatico()
objeto.retirar_dinero()
objeto.consultar_tu_saldo()
print(objeto.disponibilidad)
print(objeto.escaner_para_reconocer_tarjetas)
print(objeto.teclado_numerico)
print(objeto.pantallas_touch)
print(objeto.una_computadora)

objeto_un_cajero_automatico = cajeroautomaticoBancomer()
objeto_un_cajero_automatico.retirar_dinero()
objeto_un_cajero_automatico.consultar_tu_saldo()
objeto_un_cajero_automatico.realizar_pagos_de_servicios()
objeto_un_cajero_automatico.reconocer_y_validar_billetes()
print(objeto_un_cajero_automatico.disponibilidad)
print(objeto_un_cajero_automatico.escaner_para_reconocer_tarjetas)
print(objeto_un_cajero_automatico.teclado_numerico)
print(objeto_un_cajero_automatico.pantallas_touch)
print(objeto_un_cajero_automatico.una_computadora)
print(objeto_un_cajero_automatico.tamano)
print(objeto_un_cajero_automatico.color)
print(objeto_un_cajero_automatico.diseno)
print(objeto_un_cajero_automatico.lo_ofrece_una_institucion_bancaria)
print(objeto_un_cajero_automatico.imprime_comprobantes)