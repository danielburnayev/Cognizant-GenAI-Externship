from turtle import *

correct_responses = ["factorial", "fact", "fibonnaci", "fib", "fractal", "frac", "exit"]

while True:
    response = input("Welcome to the everything-math simulator. Choose between the following options:\n\
   - Factorial (fact)\n   - Fibonacci (fib)\n   - Fractal (frac)\n   - Exit (exit)\n\
Option: ").lower()

    if response not in correct_responses:
        print(response, "is not a provided option. Try again\n")
        continue
    if response == correct_responses[-1]:
        break
    if response == correct_responses[-3] or response == correct_responses[-2]:
        print("reached fractal\n")
    
    if response == correct_responses[0] or response == correct_responses[1]:
        print("reached factorial\n")
    if response == correct_responses[2] or response == correct_responses[3]:
        print("reached fibonnaci\n")