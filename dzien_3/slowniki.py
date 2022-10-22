tekst = "ala ma kota"
litery = {}

for i in tekst:
    try:
        litery[i] += 1
    except:
        litery[i] = 1
print(litery)

#  inna wersja
tekst = "ala ma kota"
litery = {}

for i in tekst:
    litery[i] = litery.get(i, 0) + 1
print(litery)

from collections import defaultdict

zadanytekst = "ala ma kota"
zliczenia = defaultdict(int)

for znak in zadanytekst:
    zliczenia[znak] += 1
    zliczenia[znak] = zliczenia[znak] + 1

print(zliczenia)

print(zliczenia)

import re

zadanytekst = "ala ma kota"
x = []
for i in zadanytekst:
    x.append(i + " " + str(len(re.findall(i, zadanytekst))))
print(set(x))



