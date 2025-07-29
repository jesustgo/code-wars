import re
def to_camel_case(text):
    pattern = r"[-_]"
    matchs = re.finditer(pattern, text)
    list_text = list(text)
    for match in matchs:
        list_text[match.start()] = ""
        list_text[match.end()] = str(list_text[match.end()].upper())
    text = "".join(list_text)
    return text

to_camel_case("the-stealth-warrior")