import tkinter as tk

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, score):
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = tk.Label(text=f"Score: {score}", fg="white", bg=THEME_COLOR, padx=20, pady=20)
        self.score_label.grid(row=0, column=1)

        self.canvas = tk.Canvas(width=300, height=250, highlightthickness=0, bd=0)  # Remove padx and pady
        self.q_text = self.canvas.create_text(150, 125, text="123", font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)  # Add padx and pady to the grid

        self.right_button_img = tk.PhotoImage(file='images/true.png')
        self.right_button = tk.Button(image=self.right_button_img, highlightthickness=0, padx=20, pady=20)
        self.right_button.grid(row=2, column=0)

        self.wrong_button_img = tk.PhotoImage(file='images/false.png')
        self.wrong_button = tk.Button(image=self.wrong_button_img, highlightthickness=0, padx=20, pady=20)
        self.wrong_button.grid(row=2, column=1)

        self.window.mainloop()
