# Las variables no pueden iniciar con un número, espacios o caracteres
# especiales a excepión del guion bajo (_), tampoco no se pueden llamar
# igual que las palabras reservadas:
[
    "False",
    "None",
    "True",
    "and",
    "as",
    "assert",
    "async",
    "await",
    "break",
    "class",
    "continue",
    "def",
    "del",
    "elif",
    "else",
    "except",
    "finally",
    "for",
    "from",
    "global",
    "if",
    "import",
    "in",
    "is",
    "lambda",
    "nonlocal",
    "not",
    "or",
    "pass",
    "raise",
    "return",
    "try",
    "while",
    "with",
    "yield",
]

# Declaración e inicialización de variable
a = 10
print(a)
print(type(a))

saludo = "Hello World"
print(saludo)

# Convención snake_case

saludo_en_español = "Hola Mundo"
print(saludo_en_español)

# Convención de constantes (no existen en python)

MI_CONSTANTE = "constante"

PI = 3.14159

# Tipado de variables (tampoco existe en Python como tal)
# Al ser de tipado fuerte, podemos tiparlo

# Se llaman types anottation, es documentación, no funciona como tal por el
# tipado dinámico

# En el el vscode puedes activar en configuración > Python > Analysis: Type Cheking Mode
# y ponerlo tan estricto como quieras, para que en el lint te diga los warnings, pero es como typescript, se sigue ejecutando como si nada pero el editor te avisa de que el tipo está mal

# Inicialización
num: int

# Declaración
num = 1

# Todo junto

num: int = 120
PI: float = 3.14159
name: str = "Juan"
isWorking: bool = True

# Reasignación
name = "Pedro"
print(name)

name = "Roberto"
print(name)

# no válido(tipado fuerte)
# name = 34

# Eliminación de variables

del name

# print(name)
