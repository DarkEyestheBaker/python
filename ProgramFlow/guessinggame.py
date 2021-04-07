answer = 5

print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess == answer:
    print("You got it on the first try!")
else: 
    if guess < answer:
        print("Please guess higher.")
    else:   # guess must be greater than answer
        print("Please guess lower.")
    guess = int(input())
    if guess == answer:
        print("Well, done!  You guessed it!")
    else:
        print("Sorry, you have not guessed correctly.")


# if guess < answer:
#     print("Please guess higher.")
#     guess = int(input())
#     if guess == answer:
#         print("Well done!  You guessed it!")
#     else:
#         print("Sorry, you have not guessed correctly.")
# elif guess > answer:
#     print("Please guess lower.")
#     guess = int(input())
#     if guess == answer:
#         print("Well done!  You guessed it!")
#     else:
#         print("Sorry, you have not guessed correctly.")
# else:
#     print("Well done!  You got it first time!")

# You can have one or more elif print blocks
# You don't have to include elif.
# If you have any elif lines, they come after the if.
# Elif also has to come before else if there is an else.
# You don't have to use else, but if you do, it must come after the if.
# It must also come after any elifs if there are any.