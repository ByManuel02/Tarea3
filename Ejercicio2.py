#Construir un programa que permita verificar si una persona es
#mayor de edad. Para esto debe solicitar el año de nacimiento,
#calcular la edad y si la edad es mayor o igual a 18 mostrar un
#mensaje por consola que indique que la persona es mayor de
#edad, de lo contrario que muestre un mensaje indicando que es
#menor de edad.


# Solicitar el año de nacimiento
anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
anio_actual = 2024  # Ajustar al año en curso
edad = anio_actual - anio_nacimiento

# Evaluar la mayoría de edad
if edad >= 18:
    print(f"Tienes {edad} años. Eres mayor de edad.")
else:
    print(f"Tienes {edad} años. Eres menor de edad.")
