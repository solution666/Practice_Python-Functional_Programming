def count_positives(a, b, c):
    count = 0
    if a > 0:
        count += 1
    if b > 0:
        count += 1
    if c > 0:
        count += 1
    return count

a = int(input("Введіть ціле число a: "))
b = int(input("Введіть ціле число b: "))
c = int(input("Введіть ціле число c: "))

positives_count = count_positives(a, b, c)

print("Кількість додатних чисел серед введених:", positives_count)