# --- String properties constants ---

import string

print(dir(str))

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.punctuation)
print(string.printable)
print(repr(string.whitespace))

# Methods (some of this methods are available in list too)

text = "Hola estoy aprendiendo Python"

print(text.capitalize())

print(text.lower())
print("straße".lower())

print(text.casefold())  # Like lower but more agressive
print(
    "straße".casefold()
)  # Es mejor usar casefold para hacer la comparación standard de cadenas (string1 == string2)

print(text.upper())

print("Python".center(10))
print("Python".center(10, "-"))
print("Python".center(4))

print("spam, spam, spam".count("spam"))
print(text.count("a"))
print(text.count("a", 5, 15))
print(text.count(""))
print(text.count("Juan"))

encoded_str_to_bytes = "Python".encode()
print(encoded_str_to_bytes)
print(type(encoded_str_to_bytes))
print(encoded_str_to_bytes.decode())

print(text.endswith("hon"))
print(text.endswith("N"))
print(text.endswith(("on", "do")))
print(text.endswith(("oN", "do")))
print(text.endswith("oy", 1, 10))

print(text.startswith("Ho"))

# defautl is 8
numbers = "1\t12\t123\t1234"
print(numbers.expandtabs())
print(numbers.expandtabs(4))

text2 = text + " y estoy viendo metodos de strings"
print(text2.find("estoy"))
print(text2.find("estoy", 10))
print(text2.find("estoy", 0, 10))
print(text2.find("123la"))
# Sólo devuelve la posición de la primera aparición

# reverse find
print(text2.rfind("estoy"))

# es como find pero tira un error sin no encuentra
print(text2.index("estoy"))
# print(text.index('123la')) # Error

# reverse index
print(text2.rindex("estoy"))

# Isalphanumeric pero almenos tiene que haber un caracter
print("abc123".isalnum())
print("abc123!@#".isalnum())
print("".isalnum())
print(" ".isalnum())

# Isalphabetic

print(text.isalpha())
print("LettersOnly".isalpha())
print("µ".isalpha())

# Isascii
print("ASCII characters".isascii())
print("µ".isascii())

# Isdecimal
print("0123456789".isdecimal())
print("٠١٢٣٤٥٦٧٨٩".isdecimal())  # Arabic-Indic digits zero to nine
print("alphabetic".isdecimal())

# isdigit
print("0123456789".isdigit())
print("٠١٢٣٤٥٦٧٨٩".isdigit())  # Arabic-Indic digits zero to nine
print("alphabetic".isdigit())

# isidentifier
print("hello".isidentifier())
print("12hello-world".isidentifier())

# Isnumeric
print("0123456789".isnumeric())
print("٠١٢٣٤٥٦٧٨٩".isnumeric())  # Arabic-indic digit zero to nine
print("⅕".isnumeric())  # Vulgar fraction one fifth
print("²".isdecimal(), "²".isdigit(), "²".isnumeric())

# Isspace
print("".isspace())
print(" ".isspace())
print("\t\n".isspace())
print("\u3000".isspace())  # secuencia de escape para: Ideographic space

# istitle
print("Spam, Spam".istitle())

# isupper
print("HELLO WOLRD".isupper())

# islower
print("hello wolrd".islower())

# Left justify
print("Python".ljust(10))
print("Python".ljust(10, "-"))

# Right justify
print("Python".rjust(10))
print("Python".rjust(10, "-"))

# left strip
print("   Python".lstrip())
print("www.example.com".lstrip("w."))

# right strip
print("   Python".rstrip())
print("www.example.com".rstrip("moc."))

# strip
print("   Python   ".strip())
print("www.example.com".strip("womc."))

# Remove prefix
print("TestHook".removeprefix("Test"))
print("BaseTestCase".removeprefix("Test"))

# Remove sufix
print("MiscTests".removesuffix("Tests"))
print("TmpDirMixin".removesuffix("Tests"))

# Replace
print("spam, spam, spam".replace("spam", "eggs"))
print("spam, spam, spam".replace("spam", "eggs", 1))

# Join (ver otra vez pero con listas ahora)
print("-".join("Python"))

# Swapcase
print("Hello World".swapcase())

# Title
print("Hello world".title())

# zfill
print("42".zfill(5))
print("-42".zfill(5))
