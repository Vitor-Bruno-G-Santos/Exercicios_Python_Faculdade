total = float(input("Informe o valor total da conta: R$ "))

parte_inteira = int(total // 3)
maria = float(parte_inteira)
gabriel = float(parte_inteira)
willian = total - maria - gabriel

print(f"Maria: R$ {maria:.2f}")
print(f"Gabriel: R$ {gabriel:.2f}")
print(f"Willian: R$ {willian:.2f}")
