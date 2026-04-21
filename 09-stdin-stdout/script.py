import sys

# Print

print("Hello World")  # stdout

print(sys.stdout)

day: str = "04"
year: str = "2025"
month: str = "11"

print(day, month, year, sep="-")

print("Hola", end=" ")
print("Cómo estás")

# Input
# El input SIEMPRE devuelve un string

nombre: str = input("Dime tu nombre: ")
print("Hola", nombre)

print(sys.stdin)

# mostrar una tabla de secuencias de escape ('\n', '\t', '\n', ...)
