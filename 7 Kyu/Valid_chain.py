def even_chars(st):
    if len(st) > 100 or len(st) < 2:
        return "invalid string"
    else:
        return [st[i] for i in range(1,len(st),2)]
    
st = input("Digita la secuencia: ")
print(even_chars(st))