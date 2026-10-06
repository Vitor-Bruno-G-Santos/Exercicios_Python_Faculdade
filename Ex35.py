CARNES = {
    "1": ("File Duplo", 34.90, 35.80),   # (nome, preço até 5 kg, preço acima de 5 kg)
    "2": ("Alcatra",    44.90, 46.80),
    "3": ("Picanha",    66.90, 67.80),
}
DESCONTO_CARTAO = 0.05

print("Tipos de carne: 1-File Duplo | 2-Alcatra | 3-Picanha")
tipo = input("Informe o tipo de carne: ").strip()
quantidade = float(input("Informe a quantidade (kg): "))
cartao = input("Pagamento com Cartão Tabajara? (S/N): ").strip().upper()

if tipo not in CARNES:
    print("Tipo de carne inválido!")
elif quantidade <= 0:
    print("Quantidade inválida!")
elif cartao not in ("S", "N"):
    print("Forma de pagamento inválida!")
else:
    nome, preco_ate_5, preco_acima_5 = CARNES[tipo]
    preco_kg = preco_ate_5 if quantidade <= 5 else preco_acima_5

    total = quantidade * preco_kg
    if cartao == "S":
        pagamento = "Cartão Tabajara"
        desconto = total * DESCONTO_CARTAO
    else:
        pagamento = "Outras formas"
        desconto = 0
    a_pagar = total - desconto

    print()
    print("=" * 38)
    print("     HIPERMERCADO TABAJARA")
    print("          CUPOM FISCAL")
    print("=" * 38)
    print(f"Tipo de carne:     {nome}")
    print(f"Quantidade:        {quantidade:.2f} kg")
    print(f"Preço por kg:      R$ {preco_kg:.2f}")
    print(f"Preço total:       R$ {total:.2f}")
    print(f"Tipo de pagamento: {pagamento}")
    print(f"Desconto:          R$ {desconto:.2f}")
    print(f"VALOR A PAGAR:     R$ {a_pagar:.2f}")
    print("=" * 38)