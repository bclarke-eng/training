top = int(input("Enter the maximum number you'd like to test:"))
a = str(input("Would you like to use Fizz? (y/n)"))
b = str(input("Would you like to use Buzz? (y/n)"))
c = str(input("Would you like to use Bang? (y/n)"))
d = str(input("Would you like to use Bong? (y/n)"))
e = str(input("Would you like to use Fezz? (y/n)"))
f = str(input("Would you like to use Reverse? (y/n)"))


def swap(li_st, pos1, pos2):
    li_st[pos1], li_st[pos2] = li_st[pos2], li_st[pos1]
    return li_st


for x in range(1, top + 1):
    item = []
    if x % 3 == 0 and "y" in a:
        item.append("Fizz")
    if x % 5 == 0 and "y" in b:
        item.append("Buzz")
    if x % 7 == 0 and "y" in c:
        item.append("Bang")
    if x % 11 == 0 and "y" in d:
        item.append("Bong")
    if x % 13 == 0 and "y" in e:
        item.append("Fezz")
        if "B" in item[0]:
            swap(item, 0, 1)
    if x % 17 == 0 and "y" in f and len(item) > 1:
        swap(item, 0, 1)

    if len(item) == 0:
        item.append(str(x))

    print(*item)
