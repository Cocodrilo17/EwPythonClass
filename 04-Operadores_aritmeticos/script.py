# Los operadores aritmeticos funcionan con la jerarquía de operaciones:
# 1. Parentesis ()
# 2. Exponentes
# 3. Multiplicación, division, modulo, división entera (floor division)
# 4. Suma y resta

# --- Suma ---
print("--- Suma ---")

a = 2
b = 10

print(a + b)
print(a + 2.0)  # Si sumamos o restamos un int con un float se nos devuelve un
# float

# --- Resta ---
print("--- Resta ---")

print(a - b)

# --- Multiplicacion ---
print("--- Multiplicacion ---")

print(a * b)

# --- Division ---
print("--- Division ---")

# la división siempre nos devuelve un dato float
print(b / a)
print(a / 7)
print(9 / 7)

# --- Floor Division ---
print("--- Floor Division ---")

print(9 // 7)

# --- Módulo ---
print("--- Module ---")

print(13 % 12)

# --- Exponentes ---
print("--- Exponente ---")

print(b**a)

# -- Conversión de tipos implicitas (resaltar) --
print(type(13**-1))
