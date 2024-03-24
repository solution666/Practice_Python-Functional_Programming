def distance_to_origin(x, y):
    distance = (x ** 2 + y ** 2) ** 0.5
    return distance

x1 = float(input("Введіть координату x1: "))
y1 = float(input("Введіть координату y1: "))
x2 = float(input("Введіть координату x2: "))
y2 = float(input("Введіть координату y2: "))

distance_A = distance_to_origin(x1, y1)
distance_B = distance_to_origin(x2, y2)

if distance_A < distance_B:
    print("Точка A знаходиться ближче до початку координат.")
elif distance_A > distance_B:
    print("Точка B знаходиться ближче до початку координат.")
else:
    print("Точки знаходяться на однаковій відстані до початку координат.")