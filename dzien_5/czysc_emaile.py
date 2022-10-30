import re


p = "data/emails.txt"
emails = []
emails.sort()


def zapis(line):
    line = set(line)
    with open("data/new_file.txt", "w") as f:
        for i in line:
            f.write(i)


with open(p, "r") as f:
    for i, line in enumerate(f, start=1):

        if bool(re.match(r"[\w-]+@email\.com\n", line)):
            # if line.count("@") == 1:
            new_line = ""
            for i in line:
                if i != " ":
                    new_line += i
            emails.append(new_line)
print(emails)

g = (i**2 for i in range(10))
for i in g:
    print(i)

zapis(emails)

# if __name__ == "__main":
#     main()