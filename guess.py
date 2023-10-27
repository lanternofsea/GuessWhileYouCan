
my_num = 12 #Number to guess
guess_num = True #allows the while loop to keep asking if the condition of the varaible is still "true"

while guess_num: 
    guess_num = int(input("Guess the number:")) #prompts the user to enter a number, number is turned from a string to an integer

    if guess_num == my_num: 
        print ("You Guessed it!") #if the user guesses the answer correctly, this is the outcome
        break #stops the while loop
        guess_num = False #makes the condition of the while loop false
    else:
        guess_num = True #tells the loop the condition is still true and to continue looping
        print("Try again.")
