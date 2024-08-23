pulgada = float(input("Selecciona las pulgadas a convertir "))
centimetro = float(input("Selecciona los centimetros a convertir "))

centimetros_totales = pulgada*2.54
pulgadas_totales = centimetro/2.54

print(pulgada, "pulgadas son", round(centimetros_totales, 3), "centimetros")
print(centimetro, "centimetros son", round(pulgadas_totales, 3), "pulgadas")