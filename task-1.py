def power_numbers(a, b, c):
    result = []

    for num in (a, b, c):
        if num >= 0:
            result.append(num ** 2)
        else:
            result.append(num ** 4)

    return result

num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
num3 = float(input("Введіть третє число: "))

result = power_numbers(num1, num2, num3)
print("Результати обробки чисел:", result)