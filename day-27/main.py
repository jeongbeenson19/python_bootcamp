import tkinter as tk

window = tk.Tk()
window.title("Title")
window.minsize(width=500, height=300)

my_label = tk.Label(text='Hello, World!', font=('Arial', 25, 'bold'))
my_label.pack()
window.mainloop()
