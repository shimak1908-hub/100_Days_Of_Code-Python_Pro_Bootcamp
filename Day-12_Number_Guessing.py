import random

logo=r"""
 _______           _______  _______  _______      _______      _                 _______  _______  ______   _______  _______ 
(  ____ \|\     /|(  ____ \(  ____ \(  ____ \    (  ___  )    ( (    /||\     /|(       )(       )(  ___ \ (  ____ \(  ____ )
| (    \/| )   ( || (    \/| (    \/| (    \/    | (   ) |    |  \  ( || )   ( || () () || () () || (   ) )| (    \/| (    )|
| |      | |   | || (__    | (_____ | (_____     | (___) |    |   \ | || |   | || || || || || || || (__/ / | (__    | (____)|
| | ____ | |   | ||  __)   (_____  )(_____  )    |  ___  |    | (\ \) || |   | || |(_)| || |(_)| ||  __ (  |  __)   |     __)
| | \_  )| |   | || (            ) |      ) |    | (   ) |    | | \   || |   | || |   | || |   | || (  \ \ | (      | (\ (   
| (___) || (___) || (____/\/\____) |/\____) |    | )   ( |    | )  \  || (___) || )   ( || )   ( || )___) )| (____/\| ) \ \__
(_______)(_______)(_______/\_______)\_______)    |/     \|    |/    )_)(_______)|/     \||/     \||/ \___/ (_______/|/   \__/
 """
print(logo)
print("""Welcome to the Number Guessing Game
I'm thinking a number between 1 to 100""")
number = list(range(1,101))
comp_guess = random.choice(number)
kasta = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
def yoo(guess):
    attempts = 0
    while attempts < guess:
        right_guess = int(input(f"You have {guess - attempts} attempts remaining to guess the number.\nMake a guess: "))
        attempts += 1
        if right_guess == comp_guess:
            print("Correct! You guessed it in", attempts, "attempts.")
            break  # add this line to stop after correct guess
        elif right_guess > comp_guess:
            print("Too high")
        elif right_guess < comp_guess:
            print("Too low")
    if attempts == guess and right_guess != comp_guess:
        print(f"Sorry! You have used all {guess} attempts. The number was", comp_guess)
if kasta == "easy":
    yoo(10)
else:
    yoo(5)