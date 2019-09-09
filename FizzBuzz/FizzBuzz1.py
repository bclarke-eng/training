for x in range(1, 101):  # produces all numbers from 1 to 100
    if x % 3 == 0 and x % 5 == 0:  # checks if numbers are divisible by 3 and 5
        print("Fizzbuzz")
    elif x % 3 == 0:  # checks if number is divisible by 3 only
        print("Fizz")
    elif x % 5 == 0:  # checks if number is divisible by 5 only
        print("Buzz")
    else:
        print(x)  # prints FizzBuzz list
