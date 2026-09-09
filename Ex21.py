salarioFixo = float(input("Digite o valor do salario fixo: "))
vendas = float(input("Digite o valor das vendas: "))
comissao = vendas * 0.04
print(f"Valor das comissões: R${comissao}")
print(f"Salario final: R${salarioFixo + comissao}")