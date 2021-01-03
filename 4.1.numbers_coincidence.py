x = int(input("Введіть число x: "))
y = int(input("Введіть число y: "))
z = int(input("Введіть число z: "))

if x == y == z:
    number = 3
elif (x == y) or (x == z) or (y == x) or (y == z) or (z == y) or (z == x):
    number = 2
else:
    number = 0

print(f"Кількість співпадінь: {number}")