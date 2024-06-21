# Este codigo esta implementado por medio de un Diccionario en el cual se pide la info del usuario y se guarda en el mismo

nombre = input('¿Cómo te llamas? ')
edad = input('¿Cuántos años tienes? ')
direccion = input('¿Cuál es tu dirección? ')
telefono = input('¿Cuál es tu número de teléfono? ')
persona = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono} # Creacion Diccionario
# comando print de manera que imprima el Diccionario
print("Tu nombre es: ", persona['nombre'], 'tiene', persona['edad'], 'años, vive en', persona['direccion'], 'y su número de teléfono es', persona['telefono'])