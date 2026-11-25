preco = float(input("Informe o preço normal de etiqueta: R$ "))

print("\nCondições de pagamento:")
print("1 - À vista em dinheiro ou pix (10% de desconto)")
print("2 - À vista no cartão de crédito (5% de desconto)")
print("3 - Em duas vezes, preço normal sem juros")
print("4 - Em três vezes, preço normal mais 10% de juros")

codigo = int(input("Escolha o código da condição de pagamento (1-4): "))

if codigo == 1:
    total = preco * 0.90
    print(f"Total a pagar: R$ {total:.2f}")
elif codigo == 2:
    total = preco * 0.95
    print(f"Total a pagar: R$ {total:.2f}")
elif codigo == 3:
    total = preco
    print(f"Total a pagar: R$ {total:.2f} (2x de R$ {total / 2:.2f})")
elif codigo == 4:
    total = preco * 1.10
    print(f"Total a pagar: R$ {total:.2f} (3x de R$ {total / 3:.2f})")
else:
    print("Código de pagamento inválido!")
