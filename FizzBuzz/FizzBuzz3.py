top = int(input("Enter the maximum number you'd like to test:"))

divisor = int(input("Please enter a number:"))
word = str(input("Please enter a word:"))

for x in range(1, top+1):
    item = []
    if x % divisor == 0:
        item.append(word)
    if x % divisor != 0:
        item.append(str(x))

    print(*item)
