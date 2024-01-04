import tkinter as tk


def mile_to_km():
    output = float(mile_input.get())
    output *= 1/0.62137
    km_output.config(text=output)


window = tk.Tk()
window.title("Mile to Kilometer")
window.minsize(width=300, height=100)
window.config(padx=50, pady=50)

mile_input = tk.Entry()
mile_input.grid(column=1, row=0)
mile_input.config(justify='center')

miles = tk.Label(text='Miles')
miles.grid(column=2, row=0)

is_equal_to = tk.Label(text='is equal to')
is_equal_to.grid(column=0, row=1)

km_output = tk.Label(text='0')
km_output.grid(column=1, row=1)

km = tk.Label(text='Km')
km.grid(column=2, row=1)

button = tk.Button(text='Calculate', command=mile_to_km)
button.grid(column=1, row=2)


window.mainloop()


# output = add(1, 2, 3, 4, 5, 6)
# print(output)


