secret_word = "SQL"
print("(la palabra secreta es SQL)")
while True:
    word = input("Escoge la palabra a adivinar para hacer un break en la sentencia! \n")
    if word == secret_word:
        break
print("¡Te escapaste exitosamente del loop!")