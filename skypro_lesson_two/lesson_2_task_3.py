import math
square_side = float(input("Введите число: "))
def area_of_square(square_side):
    area = float(pow(square_side, 2))
    return area

print(f"Площадь квадрата со стороной {square_side} равна {math.ceil(area_of_square(square_side))}")