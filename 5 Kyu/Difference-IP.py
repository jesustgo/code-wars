def ips_between(start, end):
    list_start, list_end = start.split("."), end.split(".")
    for i in range(0, len(list_start)):
        list_start[i] = int(list_start[i]) * 256 ** (3-i)
        list_end[i] = int(list_end[i]) * 256 ** (3-i)
    return sum(list_end) - sum(list_start)
print(ips_between("160.0.0.0", "160.0.1.0"))

# Se importa el modulo ip_address de la libreria ipaddress que contiene un metodo para poder convertir una cadena de texto a una direccion ip que se puede convertir a un entero

# from ipaddress import ip_address
# def ips_between(start, end):
#     return int(ip_address(end)) - int(ip_address(start))

# Se usa comprension de listas y 2 metodos nuevos el primero que es enumerate osea que permite saber el indice y aparte el dato que esta en ese indice para no tener que hacer 2 for uno con range y el otro para obtener el dato y el segundo es abs que es para poder devolver el valor absoluto a un numero o sea convertirlo a positivo

# def ips_between(start, end):
#     a = sum([int(e)*256**(3-i) for i, e in enumerate(start.split('.'))])
#     b = sum([int(e)*256**(3-i) for i, e in enumerate(end.split('.'))])
#     return abs(a-b)