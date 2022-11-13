import re

with open('tekst.txt', 'r') as f:
    text = f.read()
    print(re.findall("[A-z]+?-\d+?@\w+[\.\w\w\w?]+", text))
    print(re.findall("\d\d-\d{3}", text)) # 39-165
    print(re.findall("[0-3]\d \w\w\w [1-2]\d\d\d", text)) #  17 Jun 1990