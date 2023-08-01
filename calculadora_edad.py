#!/usr/bin/python3

# datetime es necesario para trabajar con fechas y horas
from datetime import datetime

# PrettyTable nos permite imprimir datos tabulados de forma ordenada en la consola
from prettytable import PrettyTable

# Pedimos los datos al usuario
nombre = input("Por favor, introduce tu nombre: ")
apellido = input("Por favor, introduce tu apellido: ")
fecha_de_nacimiento = input("Por favor, introduce tu fecha de nacimiento (dd-mm-aaaa): ")

# Convertimos la fecha de nacimiento a un objeto datetime
fecha_de_nacimiento = datetime.strptime(fecha_de_nacimiento, "%d-%m-%Y")

# Obtenemos la fecha y hora actuales
ahora = datetime.now()

# Calcular la diferencia entre ahora y la fecha de nacimiento en varias unidades de tiempo
diferencia = ahora - fecha_de_nacimiento
años = diferencia.days // 365
meses = diferencia.days // 30
semanas = diferencia.days // 7
dias = diferencia.days
horas = dias * 24
minutos = horas * 60
segundos = minutos * 60


# Creamos una tabla con PrettyTable, establecemos los nombres de los campos y añadimos los valores
tabla = PrettyTable()
tabla.field_names = ["años", "Meses", "Semanas", "Días", "Horas", "Minutos" , "Segundos"]
tabla.add_row([años, meses, semanas, dias, horas, minutos, segundos])

# Imprimimos la tabla
print(f"Hola, {nombre} {apellido}. Aquí tienes tu edad en diferentes unidades de tiempo:")
print(tabla)
