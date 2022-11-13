import json
d = {"f":"r"}

print(type(d))
print(d)
d = json.dumps(d)
print(d)
print(type(d))

import pickle

x = 1

print(pickle.dumps(x))

print(hex(1))