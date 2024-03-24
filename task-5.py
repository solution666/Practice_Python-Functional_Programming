def locate_point(x, y):
    if x > 0 and y > 0:
        return "Точка знаходиться в першому квадранті."
    elif x < 0 and y > 0:
        return "Точка знаходиться в другому квадранті."
    elif x < 0 and y < 0:
        return "Точка знаходиться в третьому квадранті."
    elif x > 0 and y < 0:
        return "Точка знаходиться в четвертому квадранті."
    elif x == 0 and y != 0:
        return "Точка знаходиться на вісі OY (ось Y)."
    elif x != 0 and y == 0:
        return "Точка знаходиться на вісі OX (ось X)."
    else:
        return "Точка знаходиться в початку координат."

x_coord = float(input("Введіть координату x точки А: "))
y_coord = float(input("Введіть координату y точки А: "))

result = locate_point(x_coord, y_coord)
print(result)