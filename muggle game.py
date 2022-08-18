# programa que lee números y se detiene al adivinar el néumero secreto
num_intentos = 0

numeroSecreto = 777

print(
"""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

# lee el primer número
numero = int (input ("Adivina el número secreto:"))

if numero == numeroSecreto:
   print("¡Bien hecho, muggle! Eres libre ahora")

else:
# "numeroSecreto" termina la ejecución
    while numero != numeroSecreto:
        # verificar si el número es 777
        if numero != numeroSecreto:
            print("¡Ja, ja! ¡Estás atrapado en mi ciclo!")
            # aumentar el contador de intentos
            num_intentos += 1
        #leer el siguiente número
        numero = int (input ("Adivina el número secreto:"))
        if numero == numeroSecreto:
            # dar la felicitación
            print("¡Bien hecho, muggle! Eres libre ahora")
# imprimir resultados
print("Números de intentos: ", num_intentos)
