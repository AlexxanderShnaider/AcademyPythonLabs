x = int(input("Введіть число: "))
y = int(input("Введіть ще одне число: "))
string = "Найменше число:"
if x > y:
    print(f"{string} {y}")
else:
    print(f"{string} {x}")