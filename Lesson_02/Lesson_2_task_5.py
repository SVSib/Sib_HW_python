def month_to_season(season):
    if 1 <= season <= 2 or season == 12:
        return "Зима"
    if 3 <= season <= 5:
        return "Весна"
    if 6 <= season <= 8:
        return "Лето"
    if 9 <= season <= 11:
        return "Осень"
    else:
        return "ошибка"


try:
    season = int(input("Введите номер месяца (1-12): "))
    print(month_to_season(season))
except ValueError:
    print("Пожалуйста, введите целое число от 1 до 12.")
