from turtle import *

def factorial(num):
    if num < 0:
        return 0
    
    if num == 0:
        return 1
    return num * factorial(num - 1)


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
        fact_input = int(input("Provide a positive integer to calculate its factorial: "))
        result = factorial(fact_input)
        print_str = str(fact_input) + "! "

        print_str += "is " + str(result) + "." if result > 0 else "cannot be calculated since " + str(fact_input) + " is not a positive number."
        print_str += "\n"

        print(print_str)

    if response == correct_responses[2] or response == correct_responses[3]:
        print("reached fibonnaci\n")