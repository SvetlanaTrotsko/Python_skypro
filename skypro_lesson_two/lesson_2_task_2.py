year = input("Введите год: ")
def is_year_leap(year):
    while True:
        try:
            year = int(year)
            break
        except ValueError:
              print("Неверный формат ввода")
              break
    if year % 4 == 0:
        return True
    if year % 4 != 0:
        return False
print(f"Год {year}: {is_year_leap(year)}")

