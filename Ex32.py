valor = int(input("Informe o valor do saque (R$): "))

if valor < 10 or valor > 600:
    print("Valor inválido! O saque deve ser de no mínimo R$ 10 e no máximo R$ 600.")
else:
    notas_100 = valor // 100
    valor = valor % 100

    notas_50 = valor // 50
    valor = valor % 50

    notas_10 = valor // 10
    valor = valor % 10

    notas_5 = valor // 5
    valor = valor % 5

    notas_1 = valor

    print("Notas fornecidas:")
    if notas_100 > 0:
        print(f"{notas_100} nota(s) de R$ 100")
    if notas_50 > 0:
        print(f"{notas_50} nota(s) de R$ 50")
    if notas_10 > 0:
        print(f"{notas_10} nota(s) de R$ 10")
    if notas_5 > 0:
        print(f"{notas_5} nota(s) de R$ 5")
    if notas_1 > 0:
        print(f"{notas_1} nota(s) de R$ 1")