secret_number = 777
numero = int(input(
"""
+================================+
| ¡Bienvenido al juego de Mate!  |
| Introducí un número entero     |
| y adivina qué número he        |
| elegido para vos.              |
|¿Cuál es el número secreto?(777)|
+================================+\n
"""))
while numero != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    numero = int(input("Elegí devuelta\n"))
print("¡Bien hecho! Ahora sos libre")