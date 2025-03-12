# Definimos la función ReemplazarCadena con tres argumentos
# cadena: frase completa
# palReemplazar: palabra o carácter a buscar para reemplazar en la cadena
# palNueva: palabra o carácter con el que se reemplazarán las ocurrencias encontradas de palReemplazar
def ReemplazarCadena(cadena, palReemplazar="o", palNueva=""):
    cadenaReemp = cadena.replace(palReemplazar, palNueva)
    return cadenaReemp

# Pedimos al usuario que introduzca una frase
fraseIntroducida = input("Introduzca una frase: ")
# Pedimos al usuario que introduzca una palabra/carácter para buscar
palBuscar = input("Introduzca la palabra/carácter a buscar: ")
# Pedimos al usuario que introduzca una palabra/carácter para reemplazar la palabra anterior si aparece
palReemplazar = input("Introduzca la palabra/carácter con el que se reemplazará: ")

# Usamos la función ReemplazarCadena
cadenaReemplazada = ReemplazarCadena(cadena=fraseIntroducida,
                                     palReemplazar=palBuscar, palNueva=palReemplazar)
# Mostramos el resultado por consola
print (f"La cadena con \"{palBuscar}\" reemplazado por \"{palReemplazar}\" es: {cadenaReemplazada}")

# Segunda parte del ejercio
# Definimos una lista
listaNumeros = ["uno", "dos", "tres", "cuatro", "cinco"]
# Usamos el iterador de orden superior map para ejecuar la función ReemplazarCadena sobre 
# todos los elementos de la lista
# Dado que en la función ReemplazarCadena hemos establecido el valor por defecto para
# palReemplazar a "o" y para palNueva a "", quitará todos los caracteres "o" que
# encuentre en cada elemento de la lista
resultado = map(ReemplazarCadena, listaNumeros)
listaResultado = list(resultado)
# Mostramos por pantalla la lista original
print(listaNumeros)
# Mostramos por pantalla la lista con la ejecución de la función ReemplazarCadena
# para todos los elementos de la lista, iterando con map
print(listaResultado)
