from tkinter import Tk, Label, Entry, Button


def suma():
    a_value = float(a.get())
    b_value = float(b.get())
    wynik.configure(text=f"{a_value + b_value}")


root = Tk()
x = "Hello Word"
label_a = Label(master=root, text="Liczba a:",)
label_a.grid(row=0, column=1)

a = Entry(master=root)
a.grid(row=1, column=1)

label_b = Label(master=root, text="Liczba b:")
label_b.grid(row=2, column=1)

b = Entry(master=root)
b.grid(row=3, column=1)

sum_btn = Button(master=root, text="DODAJ", command=suma)
sum_btn.grid(row=4, column=1)


wynik = Label(master=root, text=x)
wynik.grid(row=5, column=1)


root.mainloop()

print("To jest dopiero po loop")
