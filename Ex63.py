n = int(input("Quantos números deseja informar? "))

if n <= 0:
    print("Quantidade inválida!")
else:
    menor = None
    maior = None
    soma = 0.0

    for i in range(1, n + 1):
        valor = float(input(f"Digite o {i}º número: "))
        soma += valor
        if menor is None or valor < menor:
            menor = valor
        if maior is None or valor > maior:
            maior = valor

    print(f"Menor valor: {menor}")
    print(f"Maior valor: {maior}")
    print(f"Soma dos valores: {soma}")
