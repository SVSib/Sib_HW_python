import math


def square(x):
    return math.ceil(x * x)


num = float(input("Сторона: "))
print(f"Площадь: {square(num)}")
