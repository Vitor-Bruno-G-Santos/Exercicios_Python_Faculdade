SALARIO = 1200.00
CONTA1 = 200.00
CONTA2 = 120.00

multa1 = CONTA1 * 0.02
multa2 = CONTA2 * 0.02

restante = SALARIO - (CONTA1 + multa1) - (CONTA2 + multa2)

print(f"Restante do salário: R$ {restante:.2f}")