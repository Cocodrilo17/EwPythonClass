people: tuple[str, ...] = ("Bob", "Ben", "Brian", "Bro", "Brad")
first, second = people[0], people[1]

print(first, second)

# unpacking operator - retorna siempre una LISTA
primero, *losOtros = people
print(primero, losOtros)

primero, *_, ultimo = people
print(primero, ultimo)

numbers: list[int] = [1, 2, 3, 4, 5]
*other, y, z = numbers
print(other, y, z)

# Basic unpacking
a, b, c = [1, 2, 3]
print(a, b, c)

# Extended Iterable Unpacking with *
a, b, *c = [1, 2, 3, 4, 5]
print(a, b, c)

# Convention of ignoring values
a, _, c = [1, 2, 3]
print(a, c)

# Unpacking Nested Structures
data: tuple[str, tuple[int, str]] = "Alice", (25, "Engineer")
name, (age, profession) = data
print(name, age, profession)

# Combining Lists
list1: list[int] = [1, 2, 3]
list2: list[int] = [4, 5, 6]

combined = [*list1, *list2]
print(combined)
