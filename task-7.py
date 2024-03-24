def count_negatives(a, b, c):
    count = 0
    if a < 0:
        count += 1
    if b < 0:
        count += 1
    if c < 0:
        count += 1
    return count

a = float(input("Введіть ціле число a: "))
b = float(input("Введіть ціле число b: "))
c = float(input("Введіть ціле число c: "))

negatives_count = count_negatives(a, b, c)

print("Кількість негативних чисел серед введених:", negatives_count)