print("Actualizamos las tazas de los impuestos hace poco")
print("Vamos a analizar la cantidad actualizada a pagar que debes en base a tu ingreso correspondiente (anual)")
ingreso = float(input("Introducí el ingreso anual: "))

if ingreso <= 85528:
    impuesto = ingreso * 0.18 - 556.02
else:
    impuesto = 14839.02 + ((ingreso - 85528) * 0.32)
if impuesto < 0:
    impuesto = 0.0
impuesto = round(impuesto, 0)
print("El impuesto es:", impuesto, "pesos")
