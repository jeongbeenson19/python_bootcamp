import random

pool = ["A", 2, 3, 4, 5, 6, 7, 8, 9 ,10, 10, 10, 10, "A", 2, 3, 4, 5, 6, 7, 8, 9 ,10, 10, 10, 10, "A", 2, 3, 4, 5, 6, 7, 8, 9 ,10, 10, 10, 10, "A", 2, 3, 4, 5, 6, 7, 8, 9 ,10, 10, 10, 10]
your_hand = []
computer_hand = []
your_hand_sum = ""
computer_hand_sum = ""

def blackjack():
    global your_hand, computer_hand, your_hand_sum, computer_hand_sum
    your_hand = []
    computer_hand = []
    your_hand_sum = ""
    computer_hand_sum = ""
    #사용자에게 카드 두장 지급
    for n in range(0, 2):
        your_hand.append(pool[random.randint(0, len(pool) - 1)])
    
    #컴퓨터에게 카드 한장 지급
    computer_hand.append(pool[random.randint(0, len(pool) - 1)])

    #사용자의 히트 여부
    hit_option = input(f"Your hand is {your_hand} and computer's hand is {computer_hand} \n Do you want to hit? \n type 'y' to hit and type 'n' to stand: ")
    continuous_hit = True

    if hit_option == 'n':
        continuous_hit = False

    #사용자가 히트할 경우 실행
    while continuous_hit == True:
        #사용자의 카드에 에이스가 있을 경우 예외처리
        if "A" in your_hand:
            your_hand_sum = {}
            your_hand.remove("A")
            your_hand_sum["1"] = 1 + your_hand[0]
            your_hand_sum["10"] = 10 + your_hand[0]

        #히트 실행
        your_hand.append(pool[random.randint(0, len(pool) - 1)])

        #에이스가 있을 경우 히트한 결과 예외처리
        if type(your_hand_sum) == dict:
            your_hand_sum["1"] += your_hand[-1]
            your_hand_sum["10"] += your_hand[-1]

        #히트 결과 반영
        your_hand_sum = sum(your_hand)

        #버스트 여부 체크(에이스가 있는 경우)
        if type(your_hand_sum) != int and your_hand_sum["1"] > 21:
            print(f"your hand is {your_hand_sum}, you lose")
            if input("you wannna play once more? \n Type 'y' to retry 'n' to quit:") == 'y':
                return blackjack()
            else:
                return
            
        #버스트 여부 체크
        elif your_hand_sum >= 22:
            print(f"your hand is {your_hand_sum}, you lose")
            if input("you wannna play once more? \n Type 'y' to retry 'n' to quit:") == 'y':
                return blackjack()
            else:
                return

        #히트 추가 실행 여부
        continue_option = input(f"your hand is {your_hand_sum}, Do you want to hit once more? \n Type 'y' to hit, type 'n' to stop: ")
        if continue_option == 'n':
            continuous_hit = False

    #게임 결과 판정
    computer_hand.append(pool[random.randint(0, len(pool) - 1)])

    #컴퓨터의 카드에 에이스가 있을 경우 예외처리
    if "A" in computer_hand:
        computer_hand_sum = {}
        computer_hand.remove("A")
        computer_hand_sum["1"] = 1 + your_hand[0]
        computer_hand_sum["10"] = 10 + your_hand[0]
        if computer_hand_sum["10"] > 21:
            computer_hand_sum = computer_hand_sum["1"]
        else:
            computer_hand_sum = computer_hand_sum["10"]
    else:
        computer_hand_sum = sum(computer_hand)
        
    #컴퓨터의 카드 합이 17 미만인 경우 예외처리
    while computer_hand_sum < 17:
        print("computer has less cards number than 17, pick a card once more")
        computer_hand.append(pool[random.randint(0, len(pool) - 1)])
        
        #컴퓨터의 카드에 추가한 카드가 에이스일 경우 예외처리
        if "A" in computer_hand:
            computer_hand_sum = {}
            computer_hand.remove("A")
            computer_hand_sum["1"] = 1 + your_hand[0]
            computer_hand_sum["10"] = 10 + your_hand[0]
            if computer_hand_sum["10"] > 21:
                computer_hand_sum = computer_hand_sum["1"]
            else:
                computer_hand_sum = computer_hand_sum["10"]
        else:      
            computer_hand_sum = sum(computer_hand)

    #히트하지 않은 사용자의 카드에 에이스가 있을 경우 예외처리
    if "A" in your_hand:
        your_hand_sum = {}
        your_hand.remove("A")
        your_hand_sum["1"] = 1 + your_hand[0]
        your_hand_sum["10"] = 10 + your_hand[0]
        if your_hand_sum["10"] > 21:
            your_hand_sum = your_hand_sum["1"]
        else:
            your_hand_sum = your_hand_sum["10"]

    #사용자의 카드에 에이스가 없는 경우 게임 결과 출력
    if type(your_hand_sum) != int:
        your_hand_sum = sum(your_hand)
    if type(computer_hand_sum) != int:
        computer_hand_sum = sum(computer_hand)

    if your_hand_sum >= 22:
        print(f"your hand is {your_hand_sum}, you lose")

    elif computer_hand_sum >= 22:
        print(f"computer's hand is {computer_hand_sum}, you win") 

    elif your_hand_sum > computer_hand_sum:
        print(f"Your hand is {your_hand_sum} and computer's hand is {computer_hand_sum}, you win")
    elif your_hand_sum == computer_hand_sum:
        print(f"Your hand is {your_hand_sum} and computer's hand is {computer_hand_sum}, draw")
    else:
        print(f"Your hand is {your_hand_sum} and computer's hand is {computer_hand_sum}, you lose")

    if input("you wannna play once more? \n Type 'y' to retry 'n' to quit:") == 'y':
        return blackjack()
print("Welcome to the PyBlackJack!")
blackjack()