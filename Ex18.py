valorHora = float(input("Digite o valor da sua hora: "))
quantidadeHora = int(input("Digite a quantidade de horas trabalhadas por mês: "))

salarioBruto = valorHora * quantidadeHora
salarioLiquido = salarioBruto
totalDescontos = 0

if salarioBruto <= 900:
    print(f"Sálario bruto: ({valorHora} * {quantidadeHora}): R${salarioBruto}")
    print(f"(-) IR (ISENTO)")
elif salarioBruto <= 1500:
    print(f"Sálario bruto: ({valorHora} * {quantidadeHora}): R${salarioBruto}")
    print(f"(-) IR (5%): R${salarioBruto * 0.05}")
    salarioLiquido -= salarioBruto * 0.05
    totalDescontos += salarioBruto * 0.05
elif salarioBruto <= 2500:
    print(f"Sálario bruto: ({valorHora} * {quantidadeHora}): R${salarioBruto}")
    print(f"(-) IR (10%): R${salarioBruto * 0.1}")
    salarioLiquido -= salarioBruto * 0.1
    totalDescontos += salarioBruto * 0.1
else:
    print(f"Sálario bruto: ({valorHora} * {quantidadeHora}): R${salarioBruto}")
    print(f"(-) IR (20%): R${salarioBruto * 0.2}")
    salarioLiquido -= salarioBruto * 0.2
    totalDescontos += salarioBruto * 0.2

print(f"(-) INSS (10%) : R$ {salarioBruto * 0.1}")
salarioLiquido -= salarioBruto * 0.1
totalDescontos += salarioBruto * 0.1

print(f"FGTS (11%): R$ {salarioBruto * 0.11}")
print(f"Total de descontos: R$ {totalDescontos}")
print(f"Salario Liquido: R$ {salarioLiquido}")