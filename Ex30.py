peso = float(input("Informe o peso de peixes (kg): "))

excesso = max(0, peso - 50)
multa = excesso * 4

print(f"Peso total de peixes: {peso:.2f} kg")
print(f"Excesso: {excesso:.2f} kg")
print(f"Multa a pagar: R$ {multa:.2f}")