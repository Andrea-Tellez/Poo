class CajeroAutomatico:
  #Atributos 
  disponibilidad="las 24 horas"
  escaner_para_reconocer_tarjetas="si escanea tarjetas"
  teclado_numerico="tiene teclado numerico"
  pantallas_touch="la mayoria"
  una_computadora="si tiene una computadora"

  #Metodos
  def retirarDinero(self):
    print("retirar dinero")
  def consultarSaldo(self):
    print("consultar tu saldo")

  def __init__(self):
    print:("metodos cajero automatico")

class CajeroautomaticoBancomer (CajeroAutomatico):
  #Atributos
  tamano="estandar"
  color="depende el banco"
  diseno="estandar"
  lo_ofrece_una_institucion_bancaria="lo ofrece bancomer"
  imprime_comprobantes="imprime comprobantes"

  #Metodos
  def realizarPagosdeServicios(self):
    print("realizar pagos de servicios")
  def reconoceryValidarBilletes(self):
    print("reconocer y validar billetes")
  def retirarDinero(self):
    print("retirar dinero con tarjeta del banco")
  def consultarSaldo(self):
    print("consultar tu saldo disponible")

  def __init__(self):
    print("cajero automatico bancomer")

OBJETO=CajeroAutomatico()
OBJETO.retirarDinero()
OBJETO.consultarSaldo()
print(OBJETO.disponibilidad)
print(OBJETO.escaner_para_reconocer_tarjetas)
print(OBJETO.teclado_numerico)
print(OBJETO.pantallas_touch)
print(OBJETO.una_computadora)

OBJETO_UN_CAJERO_AUTOMATICO = CajeroautomaticoBancomer()
OBJETO_UN_CAJERO_AUTOMATICO.retirarDinero()
OBJETO_UN_CAJERO_AUTOMATICO.consultarSaldo()
OBJETO_UN_CAJERO_AUTOMATICO.realizarPagosdeServicios()
OBJETO_UN_CAJERO_AUTOMATICO.reconoceryValidarBilletes()
print(OBJETO_UN_CAJERO_AUTOMATICO.disponibilidad)
print(OBJETO_UN_CAJERO_AUTOMATICO.escaner_para_reconocer_tarjetas)
print(OBJETO_UN_CAJERO_AUTOMATICO.teclado_numerico)
print(OBJETO_UN_CAJERO_AUTOMATICO.pantallas_touch)
print(OBJETO_UN_CAJERO_AUTOMATICO.una_computadora)
print(OBJETO_UN_CAJERO_AUTOMATICO.tamano)
print(OBJETO_UN_CAJERO_AUTOMATICO.color)
print(OBJETO_UN_CAJERO_AUTOMATICO.diseno)
print(OBJETO_UN_CAJERO_AUTOMATICO.lo_ofrece_una_institucion_bancaria)
print(OBJETO_UN_CAJERO_AUTOMATICO.imprime_comprobantes)