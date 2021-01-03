import random
doors = int(input("Скільки ви хочете дверей?"))
ghost_index = 0
user_choice = 0
user_score = 0
while True:
    for i in range(doors):
        print("["+str(i + 1)+"]", end="")
    print("")
    ghost_index = random.randint(1, doors)
    user_choice = int(input("Оберіть двері:"))
    for i in range(1, doors + 1):
        if ghost_index != i:
            print("[]")
        else:
            print("[G]")
    if ghost_index == user_choice:
        print(f"Кінець! Ви протримались: {user_score}!")
        ask = input("Якщо хочете продовжити напишіть (так), якщо ні (ні)")
        if ask == "так":
            user_score = 0
            doors = int(input("Скільки ви хочете дверей?"))
            continue
        else:
            break
    else:
        user_score += 1
        print("Насупний рівень")
