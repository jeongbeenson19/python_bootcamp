import random

def hidden_number():
    target = random.randint(0, 100)

    is_valid_key = False

    while is_valid_key == False:
        game_mode = input("Welcome to the PyHiddenNumber! \n Which mode would you play? \n Type 'easy' to play game with 10 opportunities \n Type 'hard' to play game with 5 opportunities \n : ")
        
        if game_mode == 'easy':
            opportunities = 10
            is_valid_key = True
        elif game_mode == 'hard':
            opportunities = 5
            is_valid_key = True
        else:
            print("please check your answer")
    
    game_end = False
    while game_end == False:
        guess = int(input("What is your guess?: "))

        if guess == target:
            print("you win")
            game_end == True
            
        else:
            if guess > target:
                print("\n your answer is bigger than target")
            else:
                print("\n your answer is lower than target")
            opportunities -= 1
            print(f"you got a wrong answer. {opportunities} chances left. ")
        if opportunities == 0:
            print("you lose")
            game_end = True

    if input("retry? \nType 'y' to retry, 'n' to quit: ") == 'y':
        hidden_number()


hidden_number()



