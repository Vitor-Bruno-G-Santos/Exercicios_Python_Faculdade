VALOR_ALCOOL = 1.90
VALOR_GASOLINA = 2.50

litros = float(input("Informe o número de litros vendidos: "))
tipo = input("Informe o tipo de combustível (A-Álcool, G-Gasolina): ").strip().upper()

if litros <= 0:
    print("Quantidade de litros inválida!")
elif tipo == "A":
    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
    total = litros * VALOR_ALCOOL * (1 - desconto)
    print(f"Valor a pagar: R$ {total:.2f}")
elif tipo == "G":
    if litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
    total = litros * VALOR_GASOLINA * (1 - desconto)
    print(f"Valor a pagar: R$ {total:.2f}")
else:
    print("Tipo de combustível inválido!")