n = int(input("Введіть число: "))
if (n > 0) and (n <= 9):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(i, end='')
        print()
else:
    print("Неправильне значення!")
