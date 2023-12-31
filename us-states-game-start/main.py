import turtle
import pandas as pd
from location import Location

# 터틀 그래픽 초기화
screen = turtle.Screen()
location = Location()

# 맞춘 주와 놓친 주 목록 초기화
guessed_states = []
missing_states = []

# 점수 초기화
score = 0

# 터틀 그래픽 창 제목 설정
screen.title("U.S. State Quiz")


def detect_click(x, y):
    global score, guessed_states, missing_states

    # 클릭 좌표 저장
    click = (x, y)

    # 사용자 입력 받기
    answer_state = screen.textinput(title=f" {score}/50 Guess the state", prompt="What's another state's name?")

    # 주의 위치 확인
    for state in location.state_list:
        if state[1].distance(click) < 20:
            if answer_state is not None and answer_state.lower() == state[0].lower():
                # 정답 처리
                state[1].pencolor('black')
                state[1].write(state[0], align='center')
                location.clear_state(state[1])
                location.screen.update()
                score += 1
                guessed_states.append(state)
                print(f"Correct! Your score: {score}")
                return score, guessed_states
            elif answer_state is not None and answer_state.lower() != state[0].lower():
                # 오답 처리
                print("Wrong answer. Try again!")

    # 게임 종료 확인
    if answer_state == 'exit':
        # for state in location.state_list:
        #     if state not in guessed_states:
        #         guessed_state = [state[0], state[2], state[3]]
        #         missing_states.append(guessed_state)
        missing_states = [[state[0], state[2], state[3]] for state in location.state_list
                          if state not in guessed_states]

        # 놓친 주를 CSV 파일로 저장
        missing_states = pd.DataFrame(missing_states, columns=['state', 'x', 'y'])
        missing_states.to_csv('draft.csv', index=False)

        # 터틀 그래픽 종료
        turtle.bye()


# 클릭 이벤트 설정
screen.onscreenclick(detect_click)

# 터틀 그래픽 실행
screen.mainloop()
