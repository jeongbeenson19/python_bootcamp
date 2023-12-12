from random import randint
import data
import art
import os

player_profiles = data.data
game_over = False
score = 0
rounds = 14


def clear_screen():
    os.system('clear')


def get_random_player():
    return player_profiles[randint(0, len(player_profiles) - 1)]


# Display a player's information
def display_player(player):
    print(f"{player['name']} who plays for {player['team']}")


# Compare two players and prompt the user for a choice
def make_comparison(player1, player2):
    clear_screen()
    print(art.logo)
    display_player(player1)
    print(art.vs)
    display_player(player2)
    choice = input("Type '1' for the first player, '2' for the second player: ")
    return choice


# Main game loop
def main_game(a):
    global game_over, score

    current_player = a
    next_player = get_random_player()

    while next_player['value'] == current_player['value']:
        next_player = get_random_player()

    user_choice = make_comparison(current_player, next_player)

    if (user_choice == '1' and float(current_player['value']) > float(next_player['value'])) or (
            user_choice == '2' and float(next_player['value']) > float(current_player['value'])):
        score += 1
        current_player = next_player
        clear_screen()
        return current_player
    else:
        print(f"You're wrong! Your final score is {score}")
        print(
            f"{current_player['name']}'s value is {current_player['value']}"
            f"\n{next_player['name']}'s value is {next_player['value']}")
        game_over = True
        return game_over


first_player = get_random_player()
footballer = main_game(first_player)
while not game_over:
    footballer = main_game(footballer)
