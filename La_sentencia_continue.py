word_without_vowels = ""
user_word = input("Escribe tu palabra\n")
user_word = user_word.upper()
for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else: word_without_vowels += letter
print("La palabra que escribiste esta compuesta por las sioguientes consonantes:")
print(word_without_vowels)
