"""
File: class_reviews.py
Name:
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your program should be case-insensitive.
If the user input -1 for class name, your program would output
the maximum, minimum, and average among all the inputs.
"""


def main():
    """
    TODO: This program will help sorting data in relevance to scores in either SC001 or SC101.
    """
    class_name = input("Which class? ")
    if not class_name == "-1":
        sum_SC001 = 0
        count_SC001 = 0
        sum_SC101 = 0
        count_SC101 = 0
        class_name = class_name.upper()
        if class_name == "SC001":
            score = int(input("Score: "))
            sum_SC001 += score
            count_SC001 += 1
            max_SC001 = score
            min_SC001 = score
        elif class_name == "SC101":
            score = int(input("Score: "))
            sum_SC101 += score
            count_SC101 += 1
            max_SC101 = score
            min_SC101 = score
        else:
            print("Wrong input! Try again!")
        while True:
            class_name = input("Which class? ")
            class_name = class_name.upper()                         # transform the input into upper case.
            if class_name == "-1":
                break
            if class_name == "SC001":
                score = int(input("Score: "))
                sum_SC001 += score
                count_SC001 += 1
                if count_SC001 == 1:
                    max_SC001 = score
                    min_SC001 = score
                else:
                    if score >= max_SC001:
                        max_SC001 = score
                    elif score <= min_SC001:
                        min_SC001 = score
            elif class_name == "SC101":
                score = int(input("Score: "))
                sum_SC101 += score
                count_SC101 += 1
                if count_SC101 == 1:
                    max_SC101 = score
                    min_SC101 = score
                else:
                    if score >= max_SC101:
                        max_SC101 = score
                    elif score <= min_SC101:
                        min_SC101 = score
            else:
                print("Wrong input! Try again!")
        print("=============SC001=============")
        if not count_SC001 == 0:
            print(f"Max (001): {max_SC001}")
            print(f"Min (001): {min_SC001}")
            print(f"Avg (001): {sum_SC001/count_SC001}")
        else:
            print("No score for SC001")
        print("=============SC101=============")
        if not count_SC101 == 0:
            print(f"Max (101): {max_SC101}")
            print(f"Min (101): {min_SC101}")
            print(f"Avg (101): {sum_SC101/count_SC101}")
        else:
            print("No score for SC101")                                 #下面註解的code是測試用的
        # print_all(count_SC001, max_SC001, min_SC001, sum_SC001, count_SC101, max_SC101, min_SC101, sum_SC101)
    else:
        print("No class scores were entered")


# def print_all(count_SC001,max_SC001,min_SC001,sum_SC001,count_SC101,max_SC101,min_SC101,sum_SC101):
#     print("=============SC001=============")
#     if not count_SC001 == 0:
#         print(f"Max (001): {max_SC001}")
#         print(f"Min (001): {min_SC001}")
#         print(f"Avg (001): {sum_SC001 / count_SC001}")
#     else:
#         print("No score for SC001")
#     print("=============SC101=============")
#     if not count_SC101 == 0:
#         print(f"Max (101): {max_SC101}")
#         print(f"Min (101): {min_SC101}")
#         print(f"Avg (101): {sum_SC101 / count_SC101}")
#     else:
#         print("No score for SC101")




#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
