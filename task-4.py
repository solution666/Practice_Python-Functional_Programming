def replace_and_print_numbers(x, y):
    if x != y:
        smaller = min(x, y)
        bigger = max(x, y)
        
        smaller = (x + y) / 2
        bigger = x * y * 2
        
        return smaller, bigger
    else:
        print("Введені числа рівні одне одному. Спробуйте знову.")
        return None, None

x = float(input("Введіть дійсне число x: "))
y = float(input("Введіть дійсне число y: "))

smaller, bigger = replace_and_print_numbers(x, y)
if smaller is not None and bigger is not None:
    print("Менше число після заміни:", smaller)
    print("Більше число після заміни:", bigger)
