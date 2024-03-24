def find_divisors(a, b, c, k):
    divisors = []

    if k == 0:
        print("Помилка: ділення на нуль неможливе.")
        return divisors

    if a % k == 0:
        divisors.append(a)

    if b % k == 0:
        divisors.append(b)

    if c % k == 0:
        divisors.append(c)

    return divisors

a = float(input("Введіть число a: "))
b = float(input("Введіть число b: "))
c = float(input("Введіть число c: "))
k = float(input("Введіть число k: "))

divisors = find_divisors(a, b, c, k)

if divisors:
    print(f"Число {k} є дільником чисел {', '.join(map(str, divisors))}.")
else:
    print(f"Число {k} не є дільником жодного з чисел {a}, {b}, {c}.")
