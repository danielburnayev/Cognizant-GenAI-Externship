# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
#   Project Code         Project Code            Project Code          Project Code
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

import logging
logger = logging.getLogger(__name__)

def do_addition(addend1, addend2):
    return addend1 + addend2

def do_subtraction(minuend, subtrahend):
    return minuend - subtrahend

def do_multiplication(multiplier, multiplicand):
    return multiplier * multiplicand

def do_division(dividend, divisor):
    return dividend / divisor

def get_two_nums():
    print("Before computing the operation, follow the prompts below to provide two numbers on which this operation will be operated on:\n")
    while True:
        try:
            num1 = int(input("First number: "))
            num2 = int(input("Second number: "))
        except ValueError:
            print("Make sure both numbers provided are numbers. Try again.\n")
            logger.error('ValueError occured in function get_two_nums(): One of the inputs provided in this method was not a number.')
        else:
            return num1, num2

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
Selected option: ").lower()
        
        if option == given_options[-3] or option == given_options[-2] or option == given_options[-1]:
            print("See ya!")
            break
        if option not in given_options:
            print(f"\n{option} is not a valid option. Try again with something else, preferably with one given by the parentheses in the options menu.\n")
            logger.error("ValueError occured in function menu(): The provided option was not one of the valid options the calculator would accept.")
            continue

        while True:
            option_num = -1
            answer = 0
            try:
                nums = get_two_nums()
                if option in given_options[0 : 3]:
                    option_num = 0
                    answer = do_addition(nums[0], nums[1])
                elif option in given_options[4 : 7]:
                    option_num = 1
                    answer = do_subtraction(nums[0], nums[1])
                elif option in given_options[8 : 11]:
                    option_num = 2
                    answer = do_multiplication(nums[0], nums[1])
                else:
                    option_num = 3
                    answer = do_division(nums[0], nums[1])
            except ZeroDivisionError:
                print("When dividing two numbers, make sure the divisor (the second number) is not zero. Try again.\n")
                logger.error('ZeroDivisionError occured in function menu(): The divisor provided (the second number) was 0, enabling division by 0.')
            else:
                operands = ["+", "-", "*", "/"]
                print(f"\nThe answer to {nums[0]} {operands[option_num]} {nums[1]} = {answer}.\nGive the calculator another shot!\n")
                break

        


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
#     Runner Code         Runner Code            Runner Code          Runner Code
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

if __name__ == "__main__":
    logging.basicConfig(filename='error_log.txt', level=logging.ERROR)
    menu()