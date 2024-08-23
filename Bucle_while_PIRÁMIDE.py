blocks = int(input("Ingresa el número de bloques: "))
height = 0
blocks_used = 0
while blocks > 1:
    height += 1
    blocks_used += 1
    blocks = blocks - blocks_used
print("La altura de la pirámide:", height)

