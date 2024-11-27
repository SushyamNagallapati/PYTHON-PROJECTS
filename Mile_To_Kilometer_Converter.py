from tkinter import  *

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    km_result_label.config(text=f"{km}")



window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=100)
window.config(padx=20, pady=20)


# Entry
miles_input = Entry(width=10)
print(miles_input.get())
miles_input.grid(column=2, row=1)


# Label
miles_label = Label(text="Miles", font=("Ariel", 15, "normal"))
miles_label.grid(column=3, row=1)

equal_to_label = Label(text="is equal to", font=("Ariel", 15, "normal"))
equal_to_label.grid(column=1, row=2)

km_label = Label(text="Km", font=("Ariel", 15, "normal"))
km_label.grid(column=3, row=2)

km_result_label = Label(text="0")
km_result_label.grid(column=2, row=2)


calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=2, row=3)


window.mainloop()

