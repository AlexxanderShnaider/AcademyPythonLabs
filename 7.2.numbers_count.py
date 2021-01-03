count = 0
number = int(input("Введіть числа: \n"))
while number != 0:
    if number == 7:
       count += 1
    number = int(input())
print(f"Кількість чисел 7 = {count}")