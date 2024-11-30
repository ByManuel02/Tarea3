#La escuela ECAPMA de la UNAD está desarrollando un estudio para verificar el cambio climático en su ciudad. Para esto, le ha pedido su ayuda en la construcción de un programa que solicite las temperaturas de los últimos 5 días y muestre el promedio de temperaturas si el promedio es mayor o igual a 22 grados, debe informar que el clima es cálido si es menor que es frio.

# Solicitar las temperaturas de los últimos 5 días
temperaturas = []
for i in range(5):
    temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
    temperaturas.append(temp)

# Calcular el promedio
promedio = sum(temperaturas) / len(temperaturas)

# Evaluar el clima
if promedio >= 22:
    print(f"El promedio de las temperaturas es {promedio:.2f}°C. El clima es cálido.")
else:
    print(f"El promedio de las temperaturas es {promedio:.2f}°C. El clima es frío.")
