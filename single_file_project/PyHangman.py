stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
import random

words_list = ["apple"]

words_list1 = ["apple", "angel", "balloon", "block" , "chicken", "chalk", "disguise", "drill", "economy", "error" "football", "fund",
               "ground", "grill", "hypnotize", "hyundai", "ironic", "irreplaceable", "judge", "jungle", "king", "korea",
               "lemon", "league", "money", "mother", "need", "neither", "occur", "obeject", "power", "pineapple", "queen",
               "quit", "reunited", "region" "secret", "sharp", "tour", "type", "useless", "unnecessary", "victory", "victim",
               "wound", "world", "xylophone", "xray", "zebra", "zero"]
lives = 6
chosen_word = random.choice(words_list)
word_length = len(chosen_word)
end_of_game = False
blank_list = []
for n in range(0, len(chosen_word)):
    blank_list += "_"

while end_of_game == False:
    print(stages[lives])
    guess = input("What is your answer? :")
    for n in range(word_length):
        letter = chosen_word[n]
        if letter == guess:
            blank_list[n] = guess

    if not guess in chosen_word:
        lives -= 1
        print("you got a wrong answer")
        
    print(f"".join(blank_list))
    
    if not '_' in blank_list:
        end_of_game = True
        print("You win!")

    if lives == 0:
        end_of_game = True
        print(stages[lives])
        print("you lose")