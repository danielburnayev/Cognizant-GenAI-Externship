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


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
#       runner code
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
if __name__ == "__main__":
    task_one_func()