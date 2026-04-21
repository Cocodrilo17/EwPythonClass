frutas = [
    "manzana",
    "pera",
    "banana",
    "mango",
    "platano",
    1234,
    True,
    2.4,
    [True, 1234],
]

# tipar listas
lista1: list[int] = [1, 24, 15, 12]
lista2: list[str] = ["manzana", "pera"]
lista3: list[bool | str | float] = [True, "hola", 3.5]

lista4: list[list[int]] = [[3, 4, 5], [4, 5, 6]]

print(lista1)
print(frutas[0])
print(frutas[3])
print(frutas[-1])
print(frutas[2:4])

# Modify lists
frutas[0] = "naranja"
frutas[-1] = "kiwi"

print(frutas)

# revertir listas
print(lista1[::-1])

# Añadir elementos ( Con concatenación )

# Forma larga y menos eficiente
lista1 = lista1 + [10, 11, 12]
# Es menos eficiente porque primero guarda en memoria la
# operación lista1 + [10, 11, 12] luego ese valor lo guarda en lista1
# y se lo asigna
print(lista1)

# Forma corta y más eficiente
lista1 += [13, 14, 15]  # Aquí simplemente lo asigna directamente
print(lista1)

# Logitud de una lista
print(len(lista1))

# ---- Añadir un elemento al final de una lista
lista1.append(6)
print(lista1)

# ---- Instertar un elemento en una posición
lista1.insert(2, 20)
print(lista1)

# ---- Añadir varios elementos al final de la lista
lista1.extend(["hola", 7])
print(lista1)

# Diferencia del append
lista1.append([8, 9])
print(lista1)

# ---- Eliminar elementos de la lista
# Elimina la primera coincidencia de izquierda a derecha (Sólo elimina 1, aunque haya más de un 'hola' sólo va eliminar el primero)
lista1.remove("hola")
print(lista1)

# Por índice
last = (
    lista1.pop()
)  # por defecto elimina el último elemento de la lista, además te devuelve el elemento eliminado
print(last)
print(lista1)

eliminated = lista1.pop(2)
print(eliminated)
print(lista1)

# También puedes usar delete
del lista1[-1]
print(lista1)

# Con el delete puedes eliminar un rango de elementos
lista2 = ["manzana", "platano", "uva", "mango", "durazno"]
del lista2[2:3]
print(lista2)

# Eliminar todos los elementos
lista2.clear()
print(lista2)

# ----- Ordenar elementos

numbers = [2, 4, 1, 12, 13, 8, 9]
numbers.sort()
print(numbers)

# creando una copia ordenada, pero no modifica la propia lista
sorted_numbers = sorted(numbers)
print(sorted_numbers)

# Ordenar cadenas
frutas = ["manzana", "pera", "limón", "mango", "uva", "durazno"]
print(sorted(frutas))

# Ordenar cadenas con mayúsculas
frutas = ["Manzana", "Pera", "limón", "mango", "Uva", "durazno"]
print(sorted(frutas))

# Ordenar con mayúsculas pero sin que la mayúscula tenga más peso
frutas.sort(key=str.lower)
print(frutas)

# ---- Contar apariciones de elementos
frutas = ["Manzana", "Pera", "limón", "mango", "Uva", "durazno", "Manzana"]
print(frutas.count("Manzana"))

# ----- Comprobar si hay un elemento dentro
print("Durazno" in frutas)

# ver los métodos disponibles
print(dir(list))

# candenas a listas
phoneNumberList = "123-456-7890".split("-")
print(phoneNumberList)
phoneNumberList = "123-456-7890".split("-", 1)
print(phoneNumberList)

phoneNumberList = "123 456 7890".split()
print(phoneNumberList)

phoneNumberList = "123-456-7890".rsplit("-", 1)
print(phoneNumberList)

print("ab c\n\nde fg\rkl\r\n".splitlines())

print("ab c\n\nde fg\rkl\r\n".splitlines(keepends=True))

# de listas a cadenas
print("/ ".join(phoneNumberList))
