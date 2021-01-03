# TODO:
# Идеальный вес для мужчин: (рост в сантиметрах - 100) *1.15
# Идеальный вес для женщин: (рост в сантиметрах - 110) *1.15
# Пользователь должен ввести свое имя, рост и вес. Затем программа должна выдать сообщение:
# "Имя ваш идеальный вес – значение".

name = input("Enter your name: ")

# Так як не можна відняти та помножити тип str ми перетворили str на int
height = int(input("Enter your height in cm: "))
gender = input("Enter your gender: ")
coefficient = 1.15
gender_number_value = 0;

if gender == "Male":
    gender_number_value = 100
elif gender == "Female":
    gender_number_value = 110
else:
    print("Wrong gender enter!")

if gender_number_value != 0:
    ideal_weight = (height - gender_number_value) * coefficient
    print(f"{name}, your ideal weight is - {ideal_weight}.")
