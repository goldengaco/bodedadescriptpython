# Declaración de variables
nombre = "Pedro"
edad = 34
altura = 1.75
amigos = ["Juan", "Carlos", "Luis"]

# Añadiendo una nueva amiga
amigos.append("Maria")

# Convirtiendo edad a string y uniéndolo con el nombre
nombre_y_edad = nombre + " tiene " + str(edad) + " años."

# Calculando la edad en meses (asumiendo todos los años tienen 12 meses)
edad_en_meses = edad * 12

# Creando un diccionario con información
informacion = {
    "Nombre": nombre,
    "Edad": edad,
    "Altura": altura,
    "Amigos": amigos
}

# Imprimir en consola
print(nombre_y_edad)
print("Edad en meses: ", edad_en_meses)
print("Diccionario de información: ", informacion)

# Accediendo a elementos del diccionario
print("Accediendo a elementos del diccionario:")
print("Nombre desde diccionario: ", informacion["Nombre"])
print("Amigos desde diccionario: ", informacion["Amigos"])

# Verificando el tipo de cada variable
print("Tipo de nombre_y_edad: ", type(nombre_y_edad))
print("Tipo de edad_en_meses: ", type(edad_en_meses))
print("Tipo de informacion: ", type(informacion))
