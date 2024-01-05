import tkinter as tk
from tkinter import messagebox
import random

FONT = ("Courier", 10)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for n in range(5)]
    password_symbols = [random.choice(symbols) for n in range(5)]
    password_numbers = [random.choice(numbers) for n in range(5)]

    final_password = password_numbers + password_symbols + password_letters
    random.shuffle(final_password)
    final_password = "".join(final_password)

    password_entry.insert(0, final_password)
    window.clipboard_clear()
    window.clipboard_append(final_password)
    window.update()


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_password = f"{website} | {username} | {password}"
    is_ok = messagebox.askokcancel(title="My Password Manager", message=f"These are the details entered: "
                                                                        f"\nEmail: {username_entry.get()}"
                                                                        f"\nPassword: {password_entry.get()}"
                                                                        "\n is it okay to save?")
    if len(password) == 0 or len(website) == 0:
        messagebox.showinfo(title="Error", message="You have to fill all of boxes")
    else:
        with open('data.text', mode='a') as data:
            data.write(new_password + "\n")
        website_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title('My Password Manager')
window.config(padx=20, pady=20, bg='white')

canvas = tk.Canvas(width=200, height=200, bg='white', highlightthickness=0)
ui_img = tk.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=ui_img)
canvas.grid(row=0, column=1)

website_label = tk.Label(text="website", font=FONT, bg='white', fg='black', padx=10, pady=10)
website_label.grid(row=1, column=0)
website_entry = tk.Entry(width=35, bg='white', fg='black', highlightthickness=0)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

username_label = tk.Label(text="Email/Username", font=FONT, bg='white', fg='black', padx=10, pady=10)
username_label.grid(row=2, column=0)
username_entry = tk.Entry(width=35, bg='white', fg='black', highlightthickness=0)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "jeongbeenson19@gmail.com")

password_label = tk.Label(text="Password", font=FONT, bg='white', fg='black', padx=10, pady=10)
password_label.grid(row=3, column=0)
password_entry = tk.Entry(bg='white', highlightthickness=0, fg='black')
password_entry.grid(row=3, column=1)
password_button = tk.Button(text="Generate Password", command=generate_password, font=FONT, bg='white',
                            highlightthickness=0, highlightbackground='white', borderwidth=0, padx=5)
password_button.grid(row=3, column=2)

add_button = tk.Button(text="add", command=save_password, font=FONT, width=48, bg='white', highlightthickness=0,
                       highlightbackground='white',
                       borderwidth=0)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
