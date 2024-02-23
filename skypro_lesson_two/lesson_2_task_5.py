month_number = int(input("Enter a month number: "))
def month_to_season(month_number: int):
    if month_number == 1 or month_number == 2 or month_number == 12:
        return "Winter"
    elif month_number == 3 or month_number == 4 or month_number == 5:
        return "Spring"
    elif month_number == 6 or month_number == 7 or month_number == 8:
        return "Summer"
    elif month_number == 9 or month_number == 10 or month_number ==11:
        return "Fall"
    else:
        return "Invalid month number"
print(month_to_season(month_number))