soma = 0

for numero in range(1, 101):
    if numero % 2 != 0 and numero % 3 == 0:
        soma += numero

print(f"A soma é: {soma}")
