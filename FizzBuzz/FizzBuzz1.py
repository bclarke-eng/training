def fizz_buzz():
    for x in range(1, 100):
        if x % 3 == 0 and x % 5 == 0:
            return "Fizzbuzz"
        elif x % 3 == 0:
            return "Fizz"
        elif x % 5 == 0:
            return "Buzz"
        else:
            return x


print(fizz_buzz())