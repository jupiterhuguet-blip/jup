# Introduir dos numeros enters
num1 = int(input("Introdueix el primer numero: "))
num2 = int(input("Introdueix el segon numero: "))

# Suma
suma = num1 + num2
# Resta
resta = num1 - num2
# Multiplicacio
multiplicacio = num1 * num2
# Divisio
if num2 != 0:
    divisio = num1 / num2
else:
    divisio = "No es pot dividir per zero"

# Mostrar resultats
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicacio:", multiplicacio)
print("Divisio:", divisio)
