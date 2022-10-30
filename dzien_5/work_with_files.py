from pprint import pprint

f = open("praca_domowa.py")
for line in enumerate(f):
    pprint(line)
f.close()