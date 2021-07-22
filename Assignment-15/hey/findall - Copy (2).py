import re

str = "Marvellous Infosystems is in Maharashtra. Local language of Maharashtra is Marathi."

x = re.findall("Ma", str)

print(x)

x = re.findall("Pu", str)

print(x)
