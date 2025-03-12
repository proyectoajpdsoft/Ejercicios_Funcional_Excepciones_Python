# Definimos una clase Error que heredará de la clase Exception
# para mostrar un mensaje de error personalizado
class Error(Exception):
    # Definimos el constructor de la clase, con el atributo "error"
    def __init__(self, error):
        self.error = error
    # Redefinimos el método estándar __str__ para mostrar el texto pasado en el atributo "error"
    def __str__(self):
        return repr(self.error)

# Definimos la clase Persona, que no hereda de otra
class Persona (object):
    # Definimos el constructor, con los atributos DNI, nombre y apellidos
    def __init__(self, DNI="", nombre="", apellidos=""):
        self.DNI = DNI
        # Iniciamos la posible captura de errores
        try:
            # Comprobamos si el tipo de datos pasado para los atributos
            # nombre y apellidos es distinto de str (string)
            # Si es distinto, generamos la excepción con el texto personalizado
            if type(nombre) != str or type(apellidos) != str:
                raise Error("Tipo de dato no válido para el nombre o los apellidos")
            else: # Si el tipo es str, no se producirá error y se continuará la ejecución del programa
                self.nombre = nombre
                self.apellidos = apellidos                
        except Error as ex:
            self.nombre = ""
            self.apellidos = ""
            # Mostramos por consola el mensaje error personalizado
            print("Error al introducir el nombre o los apellidos:", ex.error)
        
    def __str__(self):
        return "DNI: {}, Nombre: {}, Apellidos: {}".format(
            self.DNI, self.nombre, self.apellidos)
        
# Instanciamos la clase Persona de forma correcta (sin error)
per = Persona(DNI="5252525K", nombre="Alonso", apellidos="Proyecto A")
# Mostramos por pantalla los valores de los atributos (se usará el método __str__)
print("Persona: ", per)

# Provocamos error pasando el nombre como un número
per = Persona(DNI="5252525K", nombre=1, apellidos="Pérez Díaz")
# Mostramos por pantalla los valores de los atributos (se usará el método __str__)
print("Persona: ", per)