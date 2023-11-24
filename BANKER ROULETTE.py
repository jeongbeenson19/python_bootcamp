names_string = str(input())

names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random

num_items = len(names)

random_choice = random.randint(0, num_items - 1)

banker = names[random_choice]

print(f"{banker} is going to buy the meal today!")
