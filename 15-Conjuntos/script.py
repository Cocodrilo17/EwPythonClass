my_set: set[int] = {10, 20, 30, 10}
print(my_set)  # unorder and unique values
# print(my_set[0]) no indexed
my_set.remove(20)  # Mutable
print(my_set)

# Special methods

a: set[int | str] = {10, 20, 30, 40}

a.add(50)
print(a)

# like add but you can add a lot of values
a.update([78, 12])
a.update("5634")
print(a)

a |= {1, 3}  # Update shortcut
print(a)

# like remove but it do not throws an error if don't find the element
a.discard(100)
a.discard("5")
print(a)

a.pop()  # removes a random item from the set
print(a)

# --- Math methods ---

a = {10, 20, 30, 40}
b: set[int | str] = {30, 40, 50, 60}

# Intersection
print(a.union(b))  # Gives all the values from both sets
# shortcut
print(a | b)

# Intersection
print(a.intersection(b))  # Gives the repeated values from both sets
print(a & b)

# Difference (the order matters)
print(a.difference(b))  # the values in a but not in b
print(a - b)

print(b.difference(a))
print(b - a)

# Symmetric difference
print(a.symmetric_difference(b))  # Gives the values that are not repeated form botn
print(a ^ b)

# Issubset
print(a.issubset(b))
c = {40, 60}
print(c.issubset(b))

# Issuperset
print(b.issuperset(a))
print(b.issuperset(c))

# Isdisjoint (compares if none of the values are the same)
print(a.isdisjoint(b))
d = {1, 2, 3}
print(d.isdisjoint(b))
