def is_triangle_possible(angle1, angle2):
    if angle1 + angle2 < 180:
        return True
    else:
        return False

def is_right_triangle(angle1, angle2):
    if angle1 == 90 or angle2 == 90 or (angle1 + angle2) == 90:
        return True
    else:
        return False

angle1 = float(input("Введіть величину першого кута (в градусах): "))
angle2 = float(input("Введіть величину другого кута (в градусах): "))

if is_triangle_possible(angle1, angle2):
    print("Трикутник з введеними кутами існує.")
    
    if is_right_triangle(angle1, angle2):
        print("Трикутник є прямокутним.")
    else:
        print("Трикутник не є прямокутним.")
else:
    print("Трикутник з введеними кутами не існує.")
