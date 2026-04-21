my_tuple = (10, 30, 40)

listToTuple = tuple([23, 14, "hello", "Manzana", True])

# Tuple parser: tuple()

print(my_tuple)
print(my_tuple[0])

# You can't modify a tuple
# my_tuple[1] = 120

my_tuple2: tuple[int, int, str] = 123, 141, "Hello"

print(my_tuple2)

# Sorted no modifica la tupla, te devuelve una lista
print(sorted((30, 120, 31)))

print(dir(tuple))

# Strings to tuples
print("Monty Python".partition(" "))
print("Monty Python's Flying Circus".partition(" "))
print("Monty Python".partition("-"))

# Partition Siempre devuelve una tupla con exactamente 3 elementos

# Decir que va a haber un número indefinido de elementos
numbersTuple: tuple[int, ...] = 23, 14, 15, 161, 31
