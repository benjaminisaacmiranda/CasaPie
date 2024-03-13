#if
costocasa = float(input("Ingrese el costo de la casa: "))
ingresos_comprador = float(input("Ingrese los ingresos mensuales del comprador: "))
pie = 0
pagos_mensuales = 0
if ingresos_comprador >= 80000:
    pie = 0.15 * costocasa
if ingresos_comprador < 80000:
    pie = 0.30 * costocasa
if ingresos_comprador >= 80000:
    pagos_mensuales = (costocasa - pie) / 120 
if ingresos_comprador < 80000:
    pagos_mensuales = (costocasa - pie) / 84   
print("El comprador debe pagar un pie de: ${:.2f}".format(pie))
print("Y cada pago mensual será de: ${:.2f}".format(pagos_mensuales))
