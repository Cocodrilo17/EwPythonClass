contacts = {
    "Bob": "bob@gmail.com",
    "Wendy": "wendy@hotmail.com",
    "Cecilia": "cecilia@cecilia.com",
}

print(contacts)
print(contacts["Bob"])
print(contacts["Cecilia"])

# typing

typedDict: dict[int, str] = {
    1: "a",
    2: "b",
    3: "c",
}

# Modifying

contacts["Alex"] = "alex@gmail.com"
wendy = contacts.pop("Wendy")

print(contacts)

eliminated = dict(Wendy=wendy)
print(eliminated)

# you can delete with del but it does not return the deleted value
del contacts["Bob"]

contacts["Bob"] = "bob@gmail.com"

# Devuelven iterables
print(contacts.keys())
print(contacts.values())
print(contacts.items())

# Otra forma igual que [] pero si no existe no suelta error
print(contacts.get("Bob"))
print(contacts.get("Eduardo"))
