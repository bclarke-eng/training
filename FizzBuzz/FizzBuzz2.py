def num_check(prompt):  # defining a function to check is a number is valid
    while True:
        try:
            num = int(input(prompt))  # user inputs a value for a number
        except ValueError:  # if what they input isnt a number, the user gets the message below and must retry
            print("Sorry, I didn't understand that.")
            continue
        else:
            return num


def validity(prompt):  # checks validity of user inputs where a y or n answer is needed
    while True:
        ans = str(input(prompt))  # user inputs a string value
        if ans == "y":
            break  # if user inputs y or n as required, they continue outside of the loop
        if ans == "n":
            break
        else:
            print("Sorry. That input is invalid.")  # if the input is not y or n, they have to try again
            continue
    return ans


def display_options():
    top = int(num_check("Enter the maximum number you'd like to test:\n"))  # user input for maximum range value
    a = str(validity("Would you like to use Fizz? (y/n)\n"))  # user options for which rules to use. Fizz checks if a
    # number is a multiple of 3
    b = str(validity("Would you like to use Buzz? (y/n)\n"))  # checks if its a multiple of 5
    c = str(validity("Would you like to use Bang? (y/n)\n"))  # checks if its a multiple of 7
    d = str(validity("Would you like to use Bong? (y/n)\n"))  # checks if its a multiple of 11
    e = str(validity("Would you like to use Fezz? (y/n)\n"))  # checks if its a multiple of 13
    f = str(validity("Would you like to use Reverse? (y/n)\n"))  # checks if its a multiple of 17
    h = str(validity("Would you like to use Splash?(y/n)\n")) # checks if its a multiple of 2
    g = str(validity("Would you like to set your own word for a number? (y/n)\n"))

    return top, a, b, c, d, e, f, g, h


def swap(li_st, pos1, pos2):  # defining a function that swaps the positions of 2 items in a list
    li_st[pos1], li_st[pos2] = li_st[pos2], li_st[pos1]
    return li_st


def add_user_rule(g):
    if "y" in g:
        while True:
            user_number = int(num_check("What number would you like to add a word for?"))
            if user_number == 2 or user_number == 3 or user_number == 5 or user_number == 7 or user_number == 11 or user_number == 13 or user_number == 17:
                print("Sorry. That number already has a rule assigned to it. Please enter a different number: ")
                continue
            else:
                user_word = input("Please select a word to attach the the number " + str(user_number) + ":")
                return user_number, user_word


def produce_sequence():
    top, a, b, c, d, e, f, g, h = display_options()

    user_number, user_word = add_user_rule(g)

    for x in range(1, top + 1):  # initiate a loop
        item = []  # each item (number of words in the sequence) is formatted as a type list, allowing for multiple
        # separate words to appear for each number in the sequence (say if a number is divisible by 3 and 5)
        if x % 2 == 0 and "y" in h:
            item.append("Splash")
        if x % 3 == 0 and "y" in a:
            item.append("Fizz")  # appending items to each list item in the sequence if option is selected
        if x % 5 == 0 and "y" in b:
            item.append("Buzz")
        if x % 7 == 0 and "y" in c:
            item.append("Bang")
        if x % 11 == 0 and "y" in d:
            item.append("Bong")
        if user_number is not None and x % user_number == 0:
            item.append(user_word)
        if x % 13 == 0 and "y" in e:
            item.append("Fezz")
            if "B" in item[0]:
                swap(item, 0, 1)  # if a number is divisible by 13, the word Fezz must come before all other words
                # starting with B
        if x % 17 == 0 and "y" in f and len(item) > 1:
            swap(item, 0, 1)  # if a number is divisible by 17, it swaps the order of all the words for each number

        if len(item) == 0:
            item.append(str(x))  # if a number is not divisible by 3,5,11,13 or 17 then it just prints the number

        print("".join(item))  # formats the printing in a nice-looking way


produce_sequence()
