from tkinter import *

window=Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=500,height=300)



# functions
def calculate():
    mile_to_kilo = eval(num.get())*1.609344
    result.config(text=int(mile_to_kilo))


# Labels
miles = Label(text="Miles",font=("Arial", 10))
miles.grid(column=2,row=0)
equal = Label(text="is equal to",font=("Arial", 10))
equal.grid(column=0,row=1)
km = Label(text="Km",font=("Arial", 10))
km.grid(column=2,row=1)
result = Label(text="0",font=("Arial", 10))
result.grid(column=1,row=1)

# Buttons
calc = Button(text="Calculate",command=calculate)
calc.grid(column=1,row=2)

# Entry
num = Entry(width=20)
num.grid(column=1,row=0)







window.mainloop()