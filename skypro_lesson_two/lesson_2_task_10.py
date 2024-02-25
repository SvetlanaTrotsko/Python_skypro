def bank(money, years):
    for i in range(years):
        money = money * ((1+0.1) ** years)
        money_r = round(money, 4)
        return money_r
money = float(input("Enter the amount: "))
years = int(input("Enter a year: "))
print(bank(money, years))