# tipo de dato range

nums = range(5)

print(type(nums))
print(nums)

# de range a lista
print(list(nums))

nums = range(2, 4)

print(list(nums))


# Lo que diferencia de una lista al rango es que no genera los números hasta
# que los necesitas. Por ejemplo: una lista tendría el mismo efecto, pero la
# diferencia es que la lista tienes que guardar o definir para cada posición
# en memoria los números y con range no.
nums = range(12390)
print(nums)

nums = range(5, 30, 2)
print(list(nums))

nums = range(-5, 0)
print(list(nums))

nums = range(5, 0, -1)
print(list(nums))
