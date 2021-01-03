x = int(input("Введіть число: "))
if x > 0:
    sign = 1
elif x < 0:
    sign = -1
elif x == 0:
    sign = 0
print(f"Sign({x}) = {sign}")