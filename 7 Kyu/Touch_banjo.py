def are_you_playing_banjo(name):
    name_lower = name.lower() 
    if name_lower[0] == "r": 
        return name + " plays banjo"  
    else:
        return name + " does not plays banjo"
name = input("Digita el nombre: ")
print(are_you_playing_banjo(name))