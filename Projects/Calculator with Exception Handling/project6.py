# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
#   Project Code         Project Code            Project Code          Project Code
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

def do_addition(addend1, addend2):
    return addend1 + addend2

def do_subtraction(minuend, subtrahend):
    return minuend - subtrahend

def do_multipication(multiplier, multiplicand):
    return multiplier * multiplicand

def do_division(dividend, divisor):
    return dividend / divisor

def menu():
    given_options = ["1", "a", "add", "addition",
                     "2", "s", "sub", "subtraction",
                     "3", "m", "mult", "multlipication",
                     "4", "d", "div", "division",
                     "5", "q", "quit"]

    while True:
        option = input("Welcome to my calculator! Select from the options below:\n\
\t1. Addition (add)\n\
\t2. Subtraction (sub)\n\
\t3. Multiplication (mult)\n\
\t4. Division (div)\n\
\t5. Quit (quit)\n\
\tSelected option: ").lower()
        
        if option == given_options[-3] or option == given_options[-2] or option == given_options[-1]:
            print("See ya!")
            break
        if option not in given_options:
            print(f"\n{option} is not a valid option. Try again with something else, preferably with one given by the parentheses in the options menu.\n")
            continue




# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
#     Runner Code         Runner Code            Runner Code          Runner Code
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
  
if __name__ == "__main__":
    menu()