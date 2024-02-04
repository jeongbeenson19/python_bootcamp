with open('Input/Names/invited_names.txt', mode='r') as f:
    names = f.readlines()

n = 0
for name in names:
    names[n] = name.strip()
    n += 1

for name in names:
    with open('Input/Letters/starting_letter.txt', mode='r') as ff:
        y = ff.read()
        yy = y.replace("[name]", name)
    with open(f'./Output/ReadyToSend/letter_for_{name}', mode='w') as fff:
        fff.write(yy)
        print(f'letter for {name} is saved successfully')

print(names)

