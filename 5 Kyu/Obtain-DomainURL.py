import re
def domain_name(url):
    return re.search(r"(www\.)?([\w_-]+)\.(\w+)", url).group(2)

print(domain_name("ican.org"))