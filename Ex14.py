numeroConta = int(input("Digite o numero da sua conta: "))
saldo = float(input("Digite o saldo da sua conta: "))
debitar = float(input("Digite o valor a debitar da sua conta: "))
creditar = float(input("Digite o valor a creditar na sua conta: "))

saldoAtual = saldo - debitar + creditar

print(f"Saldo atual: {saldoAtual}")
print("Saldo positivo") if saldoAtual >= 0 else print("Saldo negativo")