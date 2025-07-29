def duplicate_encode(word):
    word = word.lower()
    list_word = ["(" if word.count(letter) == 1 else ")" for letter in word]
    new_word = "".join(list_word)
    return new_word

print(duplicate_encode("oLDAAdI!jh!XrKe(@CRMUIb @@"))

# def duplicate_encode(word):
#     return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

""" Correcciones de mi codigo:
    1. Se pueden colocar varios metodos en la misma condicion
    2. La comprension de listas crea una sin nombre pero funciona como una lista
"""