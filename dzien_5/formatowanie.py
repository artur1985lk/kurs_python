# przypomneinie kwargs
import re


def formatuj(*tekst, **kwargs):
    tekst = '\n'.join(tekst)
    result = tekst
    for k,v in kwargs.items():
        for i in result:
            if i == str(k):
                result = result.replace(f'${k}', str(v))
    return result

print(formatuj("$a $b $d", a=1, b=2, c=20, d=30))

def test():
    assert formatuj("$a $b $d") == "$a $b $d"
    assert formatuj("$a $b $d", b=10) == "$a 10 $d"
    assert formatuj("$a $b $d", a=1, b=2, c=20, d=30) == "1 2 30"
    assert formatuj("$a $b", a=1, b=2, c=20, d=30) == "1 2"

# # v2
    assert formatuj("$a $b", "$a $d", a=1, b=2, c=20, d=30) == """1 2
 1 30"""

aasdfas@asdfasf.dsfa