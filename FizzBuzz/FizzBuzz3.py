def validity(prompt):  # defining a function to check is a number is valid
    while True:
        try:
            ans = int(input(prompt))  # user inputs a value for a number
        except ValueError:  # if what they input isnt a number, the user gets the message below and must retry
            print("Sorry, I didn't understand that.")
            continue
        else:
            break  # when the user inputs a number, they can move on and escape the loop
    return ans


top = int(validity("Enter the maximum number you'd like to test:\n"))  # user input for range size
divisor = int(validity("Please enter a number:\n"))  # user input for number where rule will be applied
word = str(input("Please enter a word:\n"))  # user input for a word to replace the number just entered

for x in range(1, top + 1):  # initiate for loop
    item = []  # each item (number of word in the sequence) is formatted as a type list, allowing for multiple
    # separate words to appear for each number in the sequence (say if a number is divisible by 3 and 5)
    if x % divisor == 0:  # if number in sequence is multiple of user-chosen number, replace it with the chosen word
        item.append(word)
    if x % divisor != 0:
        item.append(str(x))  # otherwise, just print the normal number

    print("".join(item))  # formats the printing in a nice-looking way
