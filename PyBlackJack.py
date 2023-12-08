import random

pool = ["A", 2, 3, 4, 5, 6, 7, 8, 9 ,10, 10, 10, 10, "A", 2, 3, 4, 5, 6, 7, 8, 9 ,10, 10, 10, 10, "A", 2, 3, 4, 5, 6, 7, 8, 9 ,10, 10, 10, 10, "A", 2, 3, 4, 5, 6, 7, 8, 9 ,10, 10, 10, 10]

def blackjack():
    your_hand = []
    computer_hand = []

    for n in range(0, 2):
        your_hand.append(pool[random.randint(0, len(pool) - 1)])
    computer_hand.append(pool[random.randint(0, len(pool) - 1)])

    hit_option = input(f"Your hand is {your_hand} and computer's hand is {computer_hand} \n Do you want to hit? \n type 'y' to hit and type 'n' to stand: ")
    continuous_hit = True
    if hit_option == 'n':
        continuous_hit = False

    while continuous_hit == True:
        your_hand.append(pool[random.randint(0, len(pool) - 1)])

        if "A" in your_hand:
            your_hand_sum = {}
            your_hand.remove("A")
            your_hand_sum["1"] = 1 + your_hand[0]
            your_hand_sum["10"] = 10 + your_hand[0]

        your_hand_sum = sum(your_hand)

        if type(your_hand_sum) != int:
            pass
        elif your_hand_sum >= 22:
            continuous_hit = False

        continue_option = input(f"your hand is {your_hand}, Do you want to hit once more? \n Type 'y' to hit, type 'n' to stop: ")
        if continue_option == 'n':
            continuous_hit = False

    computer_hand.append(pool[random.randint(0, len(pool) - 1)])

    if "A" in computer_hand:
        computer_hand_sum = {}
        computer_hand.remove("A")
        computer_hand_sum["1"] = 1 + your_hand[0]
        computer_hand_sum["10"] = 10 + your_hand[0]
        if computer_hand_sum["10"] > 21:
            computer_hand_sum = computer_hand_sum["1"]
        else:
            computer_hand_sum = computer_hand_sum["10"]
    
    while sum(computer_hand) < 17:
        computer_hand.append(pool[random.randint(0, len(pool) - 1)])

        if "A" in computer_hand:
            computer_hand_sum = {}
            computer_hand.remove("A")
            computer_hand_sum["1"] = 1 + your_hand[0]
            computer_hand_sum["10"] = 10 + your_hand[0]
            if computer_hand_sum["10"] > 21:
                computer_hand_sum = computer_hand_sum["1"]
            else:
                computer_hand_sum = computer_hand_sum["10"]

    if "A" in your_hand:
        your_hand_sum = {}
        your_hand.remove("A")
        your_hand_sum["1"] = 1 + your_hand[0]
        your_hand_sum["10"] = 10 + your_hand[0]
        if your_hand_sum["10"] > 21:
            your_hand_sum = your_hand_sum["1"]
        else:
            your_hand_sum = your_hand_sum["10"]
            
    your_hand_sum = sum(your_hand)
    computer_hand_sum = sum(computer_hand)
    if your_hand_sum >= 22:
        print(f"your hand is {your_hand}, you lose")

    if computer_hand_sum >= 22:
        print(f"computer's hand is {computer_hand}, you win") 

    if your_hand_sum > computer_hand_sum:
        print(f"Your hand is {your_hand} and computer's hand is {computer_hand}, you win")
    elif your_hand_sum == computer_hand_sum:
        print(f"Your hand is {your_hand} and computer's hand is {computer_hand}, draw")
    else:
        print(f"Your hand is {your_hand} and computer's hand is {computer_hand}, you lose")
print("Welcome to the PyBlackJack!")
blackjack()