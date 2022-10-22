import re
def więcej_niz(tekst, ile_razy):
    x = []
    for i in tekst:
        y = len(re.findall(i, tekst))

        if y > ile_razy:
            x.append(i + str(len(re.findall(i, tekst))))

    return set(x)

print(więcej_niz("ala ma kota", 2))
assert więcej_niz("ala ma kota", 2)