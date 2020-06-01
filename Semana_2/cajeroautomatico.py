class Cajero_automatico:
  #ATRIBUTOS
  disponibilidad="las 24 horas"
  escaner_para_reconocer_tarjetas="si"
  teclado_numerico="si"
  pantallas_touch="la maoyoria"
  una_computadora="si"
  tamano="pequeño"
  color="depende el banco"
  diseno="estandar"
  lo_ofrece_una_institucion_bancaria="si"
  imprime_comprobantes="si"


  #METODOS
  def retirar_dinero(self):
    print("retirar dinero")
  def consultar_tu_saldo(self):
    print("consultar tu saldo")
  def realizar_pagos_de_servicios(self):
    print("realizar pagos de servicios")
  def reconocer_y_validar_billetes(self):
    print("reconocer y validar billetes")
  def transferencia_de_fondos(self):
    print("transferencia de fondos")
  
  def __init__(self):
    print("metodos Cajero_automatico")


objeto_un_cajero_automatico = Cajero_automatico()

objeto_un_cajero_automatico.retirar_dinero()
objeto_un_cajero_automatico.consultar_tu_saldo()
objeto_un_cajero_automatico.realizar_pagos_de_servicios()
objeto_un_cajero_automatico.reconocer_y_validar_billetes()
objeto_un_cajero_automatico.transferencia_de_fondos()

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