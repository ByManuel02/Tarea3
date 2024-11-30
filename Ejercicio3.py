
#El almacén “viste con estilo” requiere de su ayuda para construir
#un programa que permita calcular la talla de ropa acorde a la
#altura ingresada así (la altura debe capturarse en centímetros):


# Solicitar la altura en centímetros
altura = int(input("Ingrese su altura en centímetros: "))

# Determinar la talla
if altura <= 150:
    talla = "S"
elif 150 < altura < 170:
    talla = "M"
elif 170 <= altura < 180:
    talla = "L"
else:
    talla = "XL"

print(f"Tu altura es {altura} cm. La talla correspondiente es {talla}.")