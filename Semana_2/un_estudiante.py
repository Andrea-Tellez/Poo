class Estudiante 
#Atributos
autodisciplina="si"
metas_definidas="si"
disposicion="si"
responsabilidad="si"
motivacion="si"
interactivo="si"
amigable="si"
creativo="si"
solidario="si"
respetuoso="si"

 #Metodos
  def hace_trabajos_escolares (self):
    print ("hace_trabajos_escolares")
  def utiiza_recursos_para_organizarse (self):
    print("utiiza_recursos_para_organizarse")
  def sigue_un_horario_escolar (self):
    print("sigue_un_horario_escolar")
  def realiza_exámenes (self):
    print ("realiza_exámenes")
  def explora_diversas_técnicas_de_estudio (self):
    print ("explora_diversas_técnicas_de_estudio")

  def __init__(self):
    print ("metodos estudiante")


objeto_un_banco= Estudiante()

objeto_un_estudiante.trabajos_escolares()
objeto_un_estudiante.utiiza_recursos_para_organizarse()
objeto_un_estudiante.sigue_un_horario_escolar()
objeto_un_estudiante.realiza_exámenes()
objeto_un_estudiante.explora_diversas_técnicas_de_estudio()


print (objeto_un_estudiante.autodisciplina)
print (objeto_un_estudiante.metas_definidas)
print (objeto_un_estudiante.disposicion)
print (objeto_un_estudiante.responsabilidad)
print (objeto_un_estudiante.motivacion)
print (objeto_un_estudiante.interactivo)
print (objeto_un_estudiante.amigable)
print (objeto_un_estudiante.creativo)
print (objeto_un_estudiante.solidario)
print (objeto_un_estudiante.respetuoso)