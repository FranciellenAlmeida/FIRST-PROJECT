inicial = int(input("Valor inicial: "))
final = int(input("Valor final: "))
passo = int(input("Passo: "))

for numero in range(inicial, final + 1, passo):
    print(numero, end=", ")
