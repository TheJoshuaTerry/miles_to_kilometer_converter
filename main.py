from tkinter import *


def calculate():
    miles = int(entered_miles.get())
    km = round(miles * 1.609)
    miles_km_label.config(text=km)


window = Tk()
window.minsize(width=300, height=200)
window.title('Miles to Kilo Converter')
window.config(padx=150, pady=30)

# Entered Miles
entered_miles = Entry(width=10)
entered_miles.grid(column=1, row=0)

# Label for Miles
miles_label = Label(text='Miles', font=('Courier', 15, 'bold'))
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=5)

# Labels for kilo converter
is_equal_label = Label(text='is equal to', font=('Courier', 15))
is_equal_label.grid(column=0, row=1)
is_equal_label.config(padx=10, pady=5)

miles_km_label = Label(text='0', font=('Courier', 15, 'bold'))
miles_km_label.grid(column=1, row=1)

km_label = Label(text='KM', font=('Courier', 15))
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=5)

# Button
button = Button(command=calculate)
button.config(text='Calculate', font=('Courier', 15, 'bold'))
button.grid(column=1, row=2)


window.mainloop()