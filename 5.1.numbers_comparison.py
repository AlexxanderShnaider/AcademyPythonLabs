a_number = int(input("Введіть число А: "))
b_number = int(input("Введіть число B: "))
if a_number > b_number:
    for i in range(a_number, b_number, -1):
        if i % 2 != 0:
            print(i)
else:
    print("Число А повинно бути більшим за число B!")
