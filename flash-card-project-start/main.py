import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
NUMBER = random.randint(1, 67)  # 랜덤한 퀴즈 번호 생성


def show_answer():
    global NUMBER  # NUMBER를 전역 변수로 선언
    card_back_img = tk.PhotoImage(file='./images/card_back.png')
    card_front.create_image(400, 263, image=card_back_img)
    card_front.itemconfigure(title, text="Answer")
    card_front.itemconfigure(content, text=df.at[NUMBER, "Answer"])


data = 'data/quiz.csv'
df = pd.read_csv(data)

window = tk.Tk()
window.title('Flash Card')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = tk.PhotoImage(file='images/card_front.png')
background = card_front.create_image(400, 263, image=card_front_img)
title = card_front.create_text(400, 150, text="Question", font=("Ariel", 40, "italic"), fill='black')
content = card_front.create_text(400, 263, text=df.at[NUMBER, "Question"], font=("Ariel", 25, "bold"), fill='black')
card_front.grid(column=0, row=0, columnspan=2)

right_img = tk.PhotoImage(file='images/right.png')
right = tk.Button(width=100, height=100, bg=BACKGROUND_COLOR, image=right_img, borderwidth=0, highlightthickness=0)
right.grid(row=1, column=1)

wrong_img = tk.PhotoImage(file='images/wrong.png')
wrong = tk.Button(width=100, height=100, bg=BACKGROUND_COLOR, image=wrong_img, borderwidth=0, highlightthickness=0)
wrong.grid(row=1, column=0)

timer = window.after(5000, func=show_answer)  # 5초 후에 정답을 보여주는 타이머 설정
window.mainloop()
