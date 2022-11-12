import re
import sys

DEBUG = False

if DEBUG:
    who = "user-6"
    file_to_write = 'wynik.txt'
else:
    who = sys.argv[1]
    file_to_write = sys.argv[2]
users = {}
list_user = []

with open('logs.txt', 'r') as f:
    text = f.readlines()
    for line in text:

        if re.search(who, line) and re.search("LOGIN", line):
            data_line = line.split(";")
            list_user.append(int(data_line[2]))
        if re.search(who, line) and re.search("LOGOUT", line):
            data_line = line.split(";")
            list_user.append(int(data_line[2]))
time_in = []
for l in range(len(list_user)):
    if l % 2 == 0:
        new_list = list_user[l] - list_user[l + 1]
        time_in.append(abs(new_list))
suma = sum(time_in)
with open(file_to_write, 'a') as f:
    f.write(who + " " + str(suma) + "\n")


