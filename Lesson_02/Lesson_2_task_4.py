n = int(input("Введите число:"))


def fizz_buzz(n):
    for i in range(1, n+1):
        if i % 3 == 0:
            print(f"{i} - fizz")
        elif i % 5 == 0:
            print(f"{i} - buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print(f"{i} - fizz_buzz")
        else:
            print(i)


fizz_buzz(n)
