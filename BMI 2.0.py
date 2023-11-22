# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆
#Write your code below this line 👇

bmi = float(weight / (height * height))

if bmi < 18.5:
  print("Your BMI is {}, you are underweight.".format(bmi))

elif 18.5 <= bmi < 25:
  print("Your BMI is {}, you have a normal weight.".format(bmi))
  
elif 25 <= bmi < 30:
  print("Your BMI is {}, you are slightly overweight.".format(bmi))

elif 30 <= bmi < 35:
  print("Your BMI is {}, you are obese.".format(bmi))

else:
  print("Your BMI is {}, you are clinically obese.".format(bmi))