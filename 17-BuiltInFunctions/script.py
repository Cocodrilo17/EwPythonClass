# Abs
print(abs(-1231))

# All - Returns True if all elements in an iterable are True
my_dict = {"Name": "Juan", "IsEmployee": True, "Age": 23}
my_dict2 = {"Name": "Juan", "IsEmployee": False, "Age": 23}

iterable = my_dict.values()
iterable2 = my_dict2.values()
print(all(iterable))
print(all(iterable2))

# Any - Returns True if any element in an iterable is True
print(any(iterable))
print(any(iterable2))

# Ascii - Returns a string containing a printable representation of an object
print(ascii("Juan"))

# Bin
print(bin(3))
print(bin(-10))

print(format(14, "#b"), format(14, "b"))
print(f"{14:#b}", f"{14:b}")

# Bool
print(bool(""))

# Breakpoint

# breakpoint()  # For debbuging, press 'h' to help

# Chr
print(chr(97))

# Enumerate - iterable
print(list(enumerate(my_dict)))
print(list(enumerate(["Spring", "Summer", "Fall", "Winter"])))

# hay muchas más funciones pero búsquen en funcion a la necesidad

# también están las Built-in Constants
