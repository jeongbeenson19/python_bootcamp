import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = tk.Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR, padx=20, pady=20)
        self.score_label.grid(row=0, column=1)

        self.canvas = tk.Canvas(width=300, height=250, highlightthickness=0, bd=0)  # Remove padx and pady
        self.question_text = self.canvas.create_text(150, 125, width=280, text="123", font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)  # Add padx and pady to the grid

        self.right_button_img = tk.PhotoImage(file='images/true.png')
        self.right_button = tk.Button(image=self.right_button_img, highlightthickness=0, padx=20, pady=20)
        self.right_button.grid(row=2, column=0)

        self.wrong_button_img = tk.PhotoImage(file='images/false.png')
        self.wrong_button = tk.Button(image=self.wrong_button_img, highlightthickness=0, padx=20, pady=20)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
