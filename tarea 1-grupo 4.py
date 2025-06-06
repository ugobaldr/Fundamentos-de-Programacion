# Constante
MENSAJE_BIENVENIDA = "=== Buscador de Números Primos en un Rango ==="

print(MENSAJE_BIENVENIDA)

# Solicitar al usuario el rango
inicio = int(input("Ingresa el número inicial del rango: "))
fin = int(input("Ingresa el número final del rango: "))

# Validación simple
if inicio > fin:
    print("El número inicial no puede ser mayor que el número final.")
    exit()

# Variable para guardar los números primos
primos_en_rango = []

# Buscar primos en el rango
for numero in range(inicio, fin + 1):
    if numero < 2:
        continue  # salta números menores que 2
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:  # Si el número es divisible por i, no es primo
            break
    else:  # Si no se encontró ningún divisor, es primo
        primos_en_rango.append(numero)

# Mostrar resultados
print(f"\nNúmeros primos entre {inicio} y {fin}:")
print(primos_en_rango)