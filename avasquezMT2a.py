#Angela Vasquez
#Course 387 Midterm

#Guess a number between 1 and 10.

x = 9

while (x != 8):
    x = float(input("Guess my number! Enter a number between 1 and 10: "))
    if (x != 8):
        print("You are incorrect, please try again.")
    if (x == 8):
        print("What an amazing guesser you are! You guessed my magic number of" ,x)

