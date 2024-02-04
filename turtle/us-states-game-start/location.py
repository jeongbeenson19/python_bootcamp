import pandas as pd
from turtle import Turtle, Screen

class Location:
    def __init__(self):
        # CSV 파일에서 데이터프레임 생성
        self.data = pd.read_csv('50_states.csv')
        self.data = pd.DataFrame(self.data)

        # 'x' 및 'y' 열을 숫자로 변환
        columns_to_convert = ['x', 'y']
        for col in columns_to_convert:
            self.data[col] = pd.to_numeric(self.data[col], errors='coerce')

        # 주의 상태 목록 및 터틀 그래픽 화면 초기화
        self.state_list = []
        self.screen = Screen()
        self.screen.bgpic("blank_states_img.gif")  # 배경 이미지 설정 (이미지 파일 필요)
        self.screen.tracer(0)  # 그래픽 업데이트 지연 해제
        self.set_state()  # 주의 상태 설정
        self.screen.update()  # 그래픽 화면 업데이트

    def set_state(self):
        # 데이터프레임을 순회하면서 주의 상태 생성
        for index, row in self.data.iterrows():
            new_t = Turtle()
            new_t.shape('circle')
            new_t.color('red')
            new_t.penup()
            new_t.shapesize(0.5, 0.5)

            # 'x' 및 'y' 열이 정수인 경우에만 처리
            if isinstance(row['x'], int) and isinstance(row['y'], int):
                x_value = int(row['x'])
                y_value = int(row['y'])
                new_t.goto(x_value, y_value)
                state = [row['state'], new_t, x_value, y_value]
                self.state_list.append(state)

    def clear_state(self, state):
        # 주의 상태를 창 밖으로 이동하여 숨김
        state.goto(1000, 1000)

