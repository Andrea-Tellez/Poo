class Palindromo:#la clase palindromo recibe la cadena y lee al reves para ver si es un palindromo
  def pali(string):
    string= string.replace(" ","")
    palindrom = ""
    for i in string:
      palindrom = i + palindrom 
    if (string == palindrom):
      print("Si es un palindromo")
    else:
      print("No es un palindromo")

class Contador:#es la clase que cuenta las vocales y espacios
  def vocales(string):#cuenta las vocales que tiene la frase o palabra
    a = string.count("a")
    e = string.count("e")
    i = string.count("i")
    o = string.count("o")
    u = string.count("u")
    count = a +e +i+o+u
    print ("La palabra o frase cuenta con :", count, " vocales")#imprime el total de vocales
  def spaces(string):
    count = string.count(" ")
    print ("La palabra o frase cuenta con :",count, " espacios")#imprime el total de espacios

respuesta = "S"
while (respuesta == "S" or respuesta == "s"):#es para repetir el proceso 
  string = []
  string = input("Igresa una palabra o una frase: ")
  s = Contador 
  s.vocales(string)
  s.spaces(string)
  st = Palindromo
  st.pali(string)
  respuesta = input ("¿Desea analizar otra cadena s/n?: ")#lee la entrada si se quiere repetir el proceso