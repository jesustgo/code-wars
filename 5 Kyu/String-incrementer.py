import re
def increment_string(strng):
    pattern = r"(\w+)(\d+)?(\w+)?(\d+)"
    if strng == "":
        return "1"
    else:
        coincidences = re.search(pattern, strng)
        
        
        return strng

increment_string("foo")