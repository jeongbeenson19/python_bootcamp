from random import randint
import data
import art
import os

player_profile = data.data
game_end = False
score = 0
number = 14

def clear():
    os.system('cls')
    
#난수 생성
def make_comparsion():
    return player_profile[randint(0, len(player_profile) - 1)]

#문제 출력
first_comparison = make_comparsion()

def HigherLower(first_comparison, score, game_end):
    if game_end == True:
        return
    clear()
    print(art.logo)
    print(f"{first_comparison['name']} who play for {first_comparison['team']}")
    print(art.vs)
    comparison = make_comparsion()

    while comparison['value'] == first_comparison['value']:
        comparison = make_comparsion()

    print(f"{comparison['name']} who play for {comparison['team']}")
    choice = input("Type '1' to choice first one, Type '2' to choice second one: ")
    
    if (choice == '1' and float(first_comparison['value']) > float(comparison['value'])) or (choice == '2' and float(comparison['value']) > float(first_comparison['value'])):
        score += 1
    else:
        print(f"you are wrong, you are final score is {score}")
        game_end = True
    
    first_comparison = comparison

    return first_comparison, score, game_end

for n in range(0, number):
    first_comparison, score, game_end = HigherLower(first_comparison, score, game_end)

    if game_end == True:
        break
