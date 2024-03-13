#while,for,else,if
costocasa = float(input("Ingrese el costo de la casa: "))
ingresos_comprador = float(input("Ingrese los ingresos mensuales del comprador: "))
if ingresos_comprador >= 80000:
    pie = 0.15 * costocasa
else:
    pie = 0.30 * costocasa
if ingresos_comprador >= 80000:
    plazo = 120  
else:
    plazo = 84   
pagos_mensuales = 0
contador = 0
while contador < plazo:
    pagos_mensuales += (costocasa - pie) / plazo
    contador += 1
print("El comprador debe pagar un pie de: ${:.2f}".format(pie))
print("Y cada pago mensual será de: ${:.2f}".format(pagos_mensuales))
