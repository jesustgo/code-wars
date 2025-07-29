def alphabet_position(text):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    text_positions = []
    for caracter in text.lower():
        for letter in alphabet:
            if letter == caracter:
                text_positions.append(str(alphabet.index(letter)+1))
    return " ".join(text_positions)

print(alphabet_position("The sunset sets at twelve o' clock."))


# El metodo ord() convierte un caracter en su codigo ascii y el metodo isalpha() revisa si la cadena contiene letras y si no esta vacia
# return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())