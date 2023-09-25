from functools import reduce

# Defina a lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usando map() para obter o quadrado de cada número
quadrados = list(map(lambda x: x**2, numeros))

# Usando filter() para obter números pares
pares = list(filter(lambda x: x % 2 == 0, numeros))

# Usando reduce() para obter a soma de todos os números
soma = reduce(lambda x, y: x + y, numeros)

print("Quadrados dos números:", quadrados)
print("Números pares:", pares)
print("Soma de todos os números:", soma)
