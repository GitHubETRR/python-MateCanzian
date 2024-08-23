print("¿Queres saber si el año en que pensas en común o bisiesto?")
año = int(input("Escribe el año:\n"))

if año < 1582:
    print("No dentro del período del calendario gregoriano")
elif año % 4 != 0:
    print(año, "Es un año común")
elif año % 100 != 0:
    print(año, "Es un año bisiesto")
elif año % 400 != 0:
    print(año, "Es un año común")
else: print(año, "Es un año bisiesto")