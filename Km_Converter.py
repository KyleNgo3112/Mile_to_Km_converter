from tkinter import *
font_text = ('font', 18, 'bold')

def mile_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    label_calculate.config(text=f"{km}")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)

#Create 3 display Labels
mile_label = Label(text="Miles", font=font_text)
mile_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to", font=font_text)
is_equal_label.grid(column=0, row=1)

km_label = Label(text="Km", font=font_text)
km_label.grid(column=2, row=1)

#create 1 calculate label
label_calculate = Label(text="0", font=font_text)
label_calculate.grid(column=1, row=1)

#Create 1 Entry
miles_input = Entry(width=10, font=font_text)
miles_input.insert(END, string="0")
miles_input.grid(column=1, row=0)

#Create 1 Button
convert_button = Button(text="Calculate", command=mile_to_km, font=font_text)
convert_button.grid(column=1, row=2)

window.mainloop()