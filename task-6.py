def replace_numbers(a, b):
    if a != b:
        return max(a, b), max(a, b)
    else:
        return 0, 0

a = float(input("Введіть ціле число a: "))
b = float(input("Введіть ціле число b: "))

a, b = replace_numbers(a, b)

print("Замінені числа:", a, b)