PRECO_PAO = 1.00
PRECO_BROA = 3.50
TAXA_POUPANCA = 0.10

paes = int(input("Informe a quantidade de pães vendidos: "))
broas = int(input("Informe a quantidade de broas vendidas: "))

total = paes * PRECO_PAO + broas * PRECO_BROA
poupanca = total * TAXA_POUPANCA

print(f"Total arrecadado: R$ {total:.2f}")
print(f"Valor a guardar na poupança: R$ {poupanca:.2f}")