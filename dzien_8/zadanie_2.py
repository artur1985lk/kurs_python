from tkinter import Tk, Label, Entry, Button
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



def suma():
    a_value = float(a.get())
    b_value = float(b.get())
    c_value = float(c.get())
    result = a_value * (b_value / 100) * c_value
    if result < 100:
        wynik.configure(text=f"{result}")
    else:
        wynik.configure(text=f"Nie jedz jest za drogo")

root = Tk()
x = ""
label_a = Label(master=root, text="Podaj spalanie samochodu:",bg='#fff', fg='#f00', pady=10, padx=10, font=10)
label_a.grid(row=0, column=1)

a = Entry(master=root)
a.grid(row=1, column=1)

label_b = Label(master=root, text="Podaj liczbę km",bg='#fff', fg='#f00', pady=10, padx=10, font=10)
label_b.grid(row=2, column=1)

b = Entry(master=root)
b.grid(row=3, column=1)

label_c = Label(master=root, text="Podaj cenę paliwa",bg='#fff', fg='#f00', pady=10, padx=10, font=10)
label_c.grid(row=4, column=1)

c = Entry(master=root)
c.grid(row=5, column=1)

sum_btn = Button(master=root, text="DODAJ", command=suma,  bg='#000', fg='#ff0', padx = 10, pady = 5)
sum_btn.grid(row=6, column=1)


wynik = Label(master=root, text=x, bg='#fff', font=30)
wynik.grid(row=7, column=1)

root.configure(background='blue')
root.mainloop()

print("To jest dopiero po loop")