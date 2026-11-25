divida = float(input("Informe o valor da dívida: R$ "))

TABELA_JUROS = [
    (1, 0),
    (3, 10),
    (6, 15),
    (9, 20),
    (12, 25),
]

print(f"\n{'Valor da Dívida':<18} {'Valor dos Juros':<18} {'Qtde Parcelas':<16} {'Valor da Parcela':<18}")
for parcelas, perc_juros in TABELA_JUROS:
    juros = divida * (perc_juros / 100)
    valor_total = divida + juros
    valor_parcela = valor_total / parcelas
    print(f"R$ {valor_total:<15.2f} R$ {juros:<15.2f} {parcelas:<15} R$ {valor_parcela:<15.2f}")
