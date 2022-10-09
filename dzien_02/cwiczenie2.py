#  pierwszy sposób

# for i in range(0,101,2):
#     print(i)


#  drugi sposób
counter = 0
while True:
    if counter % 7 == 0:
        print("Podzielny przez 7")
        print(counter)
    counter += 2


    if counter > 100:
        break


# while counter < 100:
#     print(counter)
#     counter += 2