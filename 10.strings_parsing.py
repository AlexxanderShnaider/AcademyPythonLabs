sentence = input("Введіть речення: ")  # In the hole in the ground there lived a hobbit
letter = input("Введіть букву: ")  # h

first_letter_input = sentence.find(letter)
last_letter_input = sentence.rfind(letter)
in_between_letters = sentence[first_letter_input:last_letter_input + 1]
result = sentence.replace(in_between_letters, '')
print(result)
