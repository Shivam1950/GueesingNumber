import random

class useHint:
    def __init__(self, randNum):
        self.randNum = randNum
    def getDivisor(self):
        divisor = random.randint(2, 7)
        if randNum % divisor == 0:
            print("The random number can be divided by ", divisor, ". ")
        else:
            print("The random number is NOT divisible by ", divisor, ". ")
    def getOddEven(self):
        if randNum % 2 == 0: 
            print("The Number is Evem")
        else :
            print('Number is Odd')

print("Welcome to Guess the Number")
print()
print("We are gonna generate a random number between 1 and 100, guessing correctly will give you points based on number of try and hints, good luck")
print()
randNum = random.randint(1, 100)
turns = 0
hints = 2
points = 0
flag = True
print("Random Number in generated")
print("Type 'Exit' to give up and 'Hint' to use a hint")
userhint = useHint(randNum)
while flag:
    print("Make ur guess, you have " + str(hints) + " hints remaing:")
    guessNum = input()
    if guessNum == "Exit":
        break
    elif guessNum == "Hint":
        print("Hint ->")
        if hints == 2:
            userhint.getDivisor()
            points -= 1
            hints -= 1
        elif hints == 1:
            userhint.getOddEven()
            points -= 3
            hints -= 1
        else :
            print("You have no hint left")
    else:
        try:
            guessNum = int(guessNum)
        except:
            print("Not a vaild input")
            continue
        if guessNum == randNum:
            print("Correct!, Congratulation")
            if hints == 2:
                print("You will recive extra points for a blind guess")
                points += 5
            flag = False
            turns += 1
        else:
            print("Not a correct Guess")
            if guessNum > randNum:
                print("Your Number was too high")
            else:
                print("Your Number was too low")
            print("try again!")
            turns += 1

if flag:
    print("You weren't able to guess the number, better luck next time")
else:
    if turns == 1:
        points += 10
    elif turns < 4:
        points += 9
    elif turns < 9:
        points += 7
    elif turns < 12:
        points += 5
    elif turns < 16:
        points += 3
    else:
        points += 1
    if points < 1:
        points = 0
    print("Your points: " + str(points))
