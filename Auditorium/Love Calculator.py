print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_name = name1 + name2
lovers_name = combined_name.lower()

first_digit = 0
first_digit += lovers_name.count("t")
first_digit += lovers_name.count("r")
first_digit += lovers_name.count("u")
first_digit += lovers_name.count("e")

second_digit = 0
second_digit += lovers_name.count("l")
second_digit += lovers_name.count("o")
second_digit += lovers_name.count("v")
second_digit += lovers_name.count("e")

love_score = int(str(first_digit) + str(second_digit))

if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
  
elif 40 <= love_score <= 50:
  print(f"Your score is {love_score}, you are alright together.")

else:
  print(f"Your score is {love_score}.")
