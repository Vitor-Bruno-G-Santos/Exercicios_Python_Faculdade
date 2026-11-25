menor = None
maior = None

for i in range(1, 21):
    numero = float(input(f"Digite o {i}º número: "))
    if menor is None or numero < menor:
        menor = numero
    if maior is None or numero > maior:
        maior = numero

print(f"Menor número: {menor}")
print(f"Maior número: {maior}")
