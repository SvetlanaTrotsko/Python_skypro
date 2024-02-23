def area_of_square(square_side: float):
    area = float(pow(square_side, 2))
    return area
square_side = float(input("Введите число: "))
print(f"Площадь квадрата со стороной {square_side} равна {area_of_square(square_side)}")