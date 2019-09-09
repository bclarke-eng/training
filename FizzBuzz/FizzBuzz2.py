top = int(input("Enter the maximum number you'd like to test:"))
a = str(input("Would you like to use Fizz? (y/n)"))
b = str(input("Would you like to use Buzz? (y/n)"))
c = str(input("Would you like to use Bang? (y/n)"))
d = str(input("Would you like to use Bong? (y/n)"))
e = str(input("Would you like to use Fezz? (y/n)"))

for x in range(1, top+1):
    string = ""
    if x % 3 == 0 and "y" in a:
        string = string + "Fizz"
    if x % 5 == 0 and "y" in b:
        string = string + "Buzz"
    if x % 7 == 0 and "y" in c:
        string = string + "Bang"
    if x % 11 == 0 and "y" in d:
        string = "Bong"
    if x % 13 == 0 and "y" in e:
        if "B" in string:
            string = "Fezz" + string
        else:
            string = string + "Fezz"

    else:
        string = string + str(x)
    print(string)