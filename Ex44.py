numero = int(input("Digite um número para ver a tabuada: "))

print(f"Tabuada de {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
