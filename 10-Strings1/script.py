print("List: \n\t1.Manzana\n\t2.Durazno\n\t3.Pera")

print("""\n\nList:
    1.Manzana
    2.Durazno
    3.Pera""")

# Concatenation

# 1.
greeting = "Hello " + "World"
greeting += "!"
print(greeting)

# 2
greeting = "Hello " "World"
print(greeting)

# Error: you can't concat strings and numbers
# print("your count is: " + 14)

# Explicar la estructura de datos List y porque las cadenas tienen los mismos metodos y slicing

string = "Hola estoy aprendiendo Python"
print("hola" in string)
print("Hola" in string)
print("aprendiendo" not in string)
print("python" not in string)

# Longitud
print(len(string))

# Slicing

print(string[0])
print(string[5])

print(string[1:4])
print(string[3:])
print(string[:5])
print(string[-1])
print(string[-2:])

print(string[::2])
print(string[1:-1:3])
print(string[2::2])

# revertir
print(string[::-1])

# Copia
string2 = string[:]
print(string2)

# --- Formatting ---

string = "Hello world"
print(str(string))

# la función repr() devuelve una representación legible para el interprete
print(repr(string))

x = 10 * 3.25
y = 200 * 200
print("The value of x is " + repr(x) + " and y is " + repr(y) + "...")

hello = "hello, world\n"
hellos = repr(hello)
print(hellos)

# El repr solo puede agarrar exactamente solo 1 argumento pero puedes usar tuplas para mostrar varios elementos
print(repr((x, y, ("Manzana", "Durazno"))))

# Formatted String Literlas

pi = 3.14159265358979323846
f_string = f"The value of pi is {pi}"
print(f_string)

# Redondear (más de 4 redondea hacia arriba)
print(f"The value of pi is approximately {pi:.3f}")

print("{:+f}; {:+f}".format(3.14, -3.14))  # show it always
print("{: f}; {: f}".format(3.14, -3.14))  # show a space for positive numbers
print("{:-f}; {:-f}".format(3.14, -3.14))  # show only the minus -- same as '{:f}; {:f}'

# format also supports binary numbers
print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42))

# with 0x, 0o, or 0b as prefix:
print("int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42))

print("{:,}".format(1234567890))
print("{:_}".format(1234567890))
print("{:_b}".format(1234567890))
print("{:_x}".format(1234567890))

# Percentaje
points = 19
total = 22
print("Correct answers: {:.2%}".format(points / total))


print("{:<30}".format("left aligned"))
print("{:>30}".format("right aligned"))
print("{:^30}".format("centered"))
print("{:*^30}".format("centered"))  # use '*' as a fill char

name = "Robert"
score = 21241

name2 = "Juan"
score2 = 12451

print(f"{name:10} ==> {score:10d}")
print(f"{name2:10} ==> {score2:10d}")

# !a applies ascii()
# !s applies str()
# !r applies repr()

print(ascii("Pythön"))
print("Pythön")

print("π")
print(f"{"π"!a}")

print(
    f"Louis Srygley dice: {"Sin requerimientos o diseño, programar sólo es el arte de agregar errores a un archivo vacío."!r}"
)

# operador =
isEmployee = True
print(f"Viendo a {name}: {name=} {isEmployee=} {score=}")

# Metodo Format

print("Su nombre es {} y su puntaje es {}".format(name, score))
print("Su nombre es {1} y su puntaje es {0}".format(name, score))

print("Su nombre es {name} y su puntaje es {score}".format(name="Albert", score=12315))

# Old formmating

print("The number pi is: %5.3f" % pi)
print("The number pi is: %10.3f" % pi)
