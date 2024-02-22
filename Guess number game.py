from random import  randint

#checks if number is correctly inputed
def input_numbers(num):
    while True:
        try:
            num = int(input(num))
            return num
        except ValueError:
            print("Invalid input! Please enter a valid number.")

print("\nHello! Let's start the game...")

# function allowing the user to guess a randomly generated number within a specified rang
def rang ():
    first = input_numbers("\nGuess number from: ")
    last = input_numbers("To:  ")
# checks if last number is greater than the first one, if not it swaps values.
    if first > last:
        first, last = last, first
        print("Swapped values. First number should be smaller than second!")
    
    rand_num = randint(first, last)

    # the user can choose to have limited tries and set a maximum number of attempts
    limited_tries = input("Do you want to have limited tries? (yes/no): ").lower().strip()
    if limited_tries == 'yes':
        max_tries = input_numbers("Enter number of tries: ")
    else:
        max_tries = None
    tries = 0
    while max_tries is None or tries < max_tries:
        tries +=1
        n = input_numbers("\nEnter number: ")
        if n == rand_num :
            if tries ==  1:
                print(f"0(=o=)0 Wow! You guessed it right on your first try! You're a natural!.\n")
                break
            else:
                print(f"Correct! Good job d(^∇^)b, it only took you {tries} tries.\n")
                break  
        elif n > rand_num:
            print("Too big, try again")
            continue
        else:
            print("Too small, try again")
            continue
    else:
        print("Sorry, you've run out of tries (◞‸◟；) The correct number was:", rand_num)

# function checks if user wants to play again or not
while True:
    rang()
    play_again = input("Do you want to play again? (yes/no): ").lower().strip()
    if play_again != 'yes':
        print("\nThank you for playing! Goodbyeヾ(•ω•`)o")
        break

