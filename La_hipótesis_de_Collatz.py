c0 = int(input("Elige el número\n"))
if c0 <= 0:
    c0 = int(input("Elige el número entero positivo\n"))
while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 / 2

    else:
        c0 = 3 * c0 + 1
    print(c0)