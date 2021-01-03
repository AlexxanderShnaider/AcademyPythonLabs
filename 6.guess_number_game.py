import random

while True:
    plays_counter = 0
    number = random.randint(1, 10)
    guess = int(input("Я загадав число від 1 до 10. Яке ж число я загадав?\n"))
    plays_counter += 1
    while guess != number:
        if guess < number:
            print("Ваше число занадто мале.")
        elif guess > 10:
            print("Ваше число не підходить, спробуйте ще раз!")
        elif guess > number:
            print("Ваше число занадто велике.")
            continue
        guess = int(input("Будь ласка спробуйте ще раз.\n"))
        plays_counter += 1
    print(f"Мої вітання! Правильна відповідь з {plays_counter} спроби! Кількість неправильних спроб = {plays_counter - 1}")
    reply = input("Введіть 'ТАК', якщо хочете продовжити гру. Якщо не хочете продовжувати гру, введіть 'НІ'\n").lower()
    if reply == 'ні':
        break
