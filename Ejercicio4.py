#La empresa Netflix desea saber cuál es el género favorito de
#streaming entre 5 personas. Para esto, le ha solicitado su ayuda
#para desarrollar un programa para saber cuál es el género con
#más votos entre: acción y ciencia ficción. El programa debe
#apturar la preferencia de las 5 personas y mostrar cuál de los
#géneros es el favorito.

# Inicializar contadores
accion = 0
ciencia_ficcion = 0

# Capturar las preferencias de 5 personas
for i in range(5):
    genero = input(f"Persona {i+1}, ¿prefieres acción o ciencia ficción?: ").lower()
    if genero == "acción":
        accion += 1
    elif genero == "ciencia ficción":
        ciencia_ficcion += 1

# Determinar el género favorito
if accion > ciencia_ficcion:
    print(f"El género favorito es Acción con {accion} votos.")
elif ciencia_ficcion > accion:
    print(f"El género favorito es Ciencia Ficción con {ciencia_ficcion} votos.")
else:
    print("Ambos géneros tienen la misma cantidad de votos.")
