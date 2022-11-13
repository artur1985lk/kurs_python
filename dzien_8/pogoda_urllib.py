import json
import requests

url = "https://api.nbp.pl/api/exchangerates/tables/C?format=json"
r = requests.get(url)
date = r.json()
waluta = json.dumps(date)
w = json.loads(waluta)
# print(w)
kurs = 0
new = dict(w[0])
new = new['rates']
for v in new:
    x = dict(v)
    print(x['code'], end=" ")
print()
jaka = input("jaką walute ").upper()
ile = input("ile chcesz kupić ")


for v in new:
    x = dict(v)
    if x['code'] == jaka:
        kurs = x['bid']
        print(x['bid'])

print("Musisz mieć ", float(kurs) * float(ile))
