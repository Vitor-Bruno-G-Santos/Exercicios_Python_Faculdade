CARDAPIO = {
    1: ("Bife acebolado", 15.00),
    2: ("Lasanha", 25.00),
    3: ("Frango à parmegiana", 28.00),
    4: ("Strogonoff de carne", 24.00),
    5: ("Feijoada completa", 32.00),
    6: ("Macarrão à bolonhesa", 20.00),
}

print("=== CARDÁPIO ===")
for codigo, (prato, valor) in CARDAPIO.items():
    print(f"{codigo} - {prato} - R$ {valor:.2f}")

escolha = int(input("\nEscolha o número do prato desejado: "))

if escolha not in CARDAPIO:
    print("Opção inválida!")
else:
    prato, valor = CARDAPIO[escolha]
    gorjeta = input("Aceita pagar a gorjeta do garçom (10% sobre o valor do prato)? (S/N): ").strip().upper()
    if gorjeta == "S":
        valor_final = valor * 1.10
    else:
        valor_final = valor
    print(f"Prato escolhido: {prato}")
    print(f"Valor final a pagar: R$ {valor_final:.2f}")
