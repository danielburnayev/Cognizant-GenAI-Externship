# task 1
def divide_one_hundred_by_num():
    try:
        prompt_num = int(input("Enter a number so that 100 can be divided by it: "))
        answer = 100 / prompt_num
    except ValueError:
        print("The input provided needs to be a number! Try running this program again with a different input.\n")
    except ZeroDivisionError:
        print("The input provided cannot be the number zero! Try running this program again with a different input.\n")
    else:
        print(f"100 / {prompt_num} = {100 / prompt_num}.\n")

def task_one_func():
    divide_one_hundred_by_num()


# task 2
class CustomInvalidRangeError(Exception):
    pass    

def force_index_error():
    nums = [1, 2, 3, 4, 5]
    return nums[100]

def force_key_error():
    example_dict = {"a": 1, "b": 4, "c": 0, "d": 21}
    return example_dict["z"]

def force_type_error():
    wrong_str = "wrong " + 1
    return wrong_str

def task_two_func():
    while True:
        try:
            response = int(input("Welcome to the error inducer! Select the type of error to be forced by typing out one of the numbers below:\n\
\t1. Index Error\n\
\t2. Key Error\n\
\t3. Type Error\n\
\t4. Quit (Not an error, just exiting out of the program)\n\
Input: "))
            
            if response == 1:
                force_index_error()
            if response == 2:
                force_key_error()
            if response == 3:
                force_type_error()

            if response < 1 or response > 4:
                raise CustomInvalidRangeError()
            
        except IndexError: 
            print("Here, an IndexError is caused because index 100 cannot be accessed in the 5-length list [1, 2, 3, 4, 5].\n")
        except KeyError: 
            print("Here, a KeyError is caused because key \"z\" cannot be accessed in dictionary {\"a\": 1, \"b\": 4, \"c\": 0, \"d\": 21}.\n")
        except TypeError: 
            print("Here, a TypeError is caused because string \"wrong\" and number 1 cannot be concatenated together.\n")
        except ValueError:
            print(f"While not one of the proposed errors, a ValueError happened here because the given input, {response}, was not a number as expected.\n")
        except CustomInvalidRangeError:
            print(f"While not one of the proposed errors, a CustomInvalidRangeError (one I made myself) happened because the given input, {response}, while a number, is not a number from 1 to 4.\n")
        else:
            break


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
#       runner code
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
if __name__ == "__main__":
    task_one_func()
    task_two_func()