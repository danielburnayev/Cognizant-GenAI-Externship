# getting the age input from the user via. terminal (needs to be an int, otherwise this goes kaput)
age = int(input("How old are you? THIS MUST BE A INTEGER!\n"))
# here to easily change the minimum age to vote (in case the minimum age gets used more often in code)
min_age = 18

if age >= min_age:
    print("Congratulations! You are eligible to vote. Go make a difference!")
elif age < 0:
    print("No, that's not how that works. You can't be negative years old. Redo this.")
else:
    # variable of the age gap left for simplicity in code
    diff = min_age - age
    print("Oops! You're not eligible yet. But hey, only", diff, "more", "years" if diff > 1 else "year", "to go!")