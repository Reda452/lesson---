import random # importing module
playing = True #initialise
number = str(random.randint(10,20)) #random in-built function

print (" I will generate a number from 10 to 20, you have to guess the number one digit at a time.")
print (" the game ends when you get 1 hero!")
# literate loop till the condition is true
while playing:
     guess = input("give me your best guesse! \n")
     if number == guess:
        print (" You win the game")
        print("The number was", number)
        break
    
else:
    print(" Your guess isn't quite right, try again \n")