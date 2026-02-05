dato = input("Escribe un dato cualquiera ")

try:
    entero = int(dato)
    print("El dato que usted ingreso es ", entero, " y es de tipo entero.")
except ValueError:
    pass

print("Fin de la ejecucuión")