from turtle import *

def factorial(num):
    if num < 0:
        return 0
    
    if num == 0:
        return 1
    return num * factorial(num - 1)

def fibonnaci(num):
    if num < 0:
        return -1
    
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibonnaci(num - 2) + fibonnaci(num - 1)

def do_simple_function(input_prompt, input_method, word):
    given_input = int(input(input_prompt))
    result = input_method(given_input)
    print_str = str(given_input) + "! "

    print_result(print_str, result, word, given_input)

def print_result(the_str, result, word, input):
    the_str += "is " + str(result) + "." if result > 0 else "cannot be " + word + " since " + str(input) + " is not a positive number."
    the_str += "\n"
    print(the_str)


# -------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------
# runner code start
# -------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------
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
        do_simple_function("Provide a positive integer to calculate its factorial: ", factorial, "calculated")

    if response == correct_responses[2] or response == correct_responses[3]:
        do_simple_function("Provide a positive integer to determine the nth value in the Fibonnaci sequence: ", fibonnaci, "determined")
    
