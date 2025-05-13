import random
number_to_guess = random.randint(1, 100)

attempts_made = 0
attempts_allowed = 10

while attempts_made < attempts_allowed:
    selected_num = int(input("Guess a number from 1 to 100, any number! You have " + str(attempts_allowed - attempts_made) + (" attempt" if attempts_made == 9 else " attempts") + " left. "))
    if selected_num < 1:
        print("Ok, that's too low. Try to keep your next guesses in between 1 and 100.")
    elif selected_num > 100:
        print("Ok, that's too high. Try to keep your next guesses in between 1 and 100.")
    elif selected_num < number_to_guess:
        print("Too low! Try again.")
    elif selected_num > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number", number_to_guess, "in", attempts_made + 1, "attempt!" if attempts_made == 0 else "attempts!")
        break

    attempts_made += 1

if attempts_made == attempts_allowed:
    print("Unfortunately, you used up all of your", attempts_allowed, "attempts and didn't guess the number", number_to_guess, ". Run this program again to get another shot at it with a (possibly) new random number!")