while True:   
    cadena = input("hola mundo")   #es la entrada de texto
    for caracter in cadena: #lee el texto de los caracteres
        print('"{}"'.format(caracter)) #imprime cada caracter 
        if caracter.isalpha():  #analiza si es letra
            print("letra") #imprime el resultado
        elif caracter.isnumeric("numero"): #analiza si es numero
            print("numero") 
        else:  #es el ultimo recurso en caso que no sean las anteriores
            print() 
    print("numero de caracteres: ",len(cadena)) #imprime la longuitud de la cadena
    sin_espacios = cadena.replace(" ", "") #elimina los espacios 
    print("numero de caracteres sin espacios: ",len(sin_espacios)) #imprime la longuitud de la cadena sin espacios
    otra = input("¿Desea analizar otra cadena si/no?: ") #entrada de texto para el bucle si se repite o no
    if not (otra == "s1" or otra == "SI"): 
        break 
