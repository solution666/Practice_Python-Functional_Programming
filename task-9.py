def count_integers(a, b, c):
    count = 0
    if a.replace('-', '').isdigit():
        count += 1
    elif '.' in a and float(a).is_integer():
        count += 1

    if b.replace('-', '').isdigit():
        count += 1
    elif '.' in b and float(b).is_integer():
        count += 1

    if b.replace('-', '').isdigit():
        count += 1
    elif '.' in c and float(c).is_integer():
        count += 1

    return count

a = input("Введіть число a: ")
b = input("Введіть число b: ")
c = input("Введіть число c: ")

integers_count = count_integers(a, b, c)

print("Кількість цілих чисел серед введених:", integers_count)
