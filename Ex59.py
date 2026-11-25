n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))

inicio = min(n1, n2)
fim = max(n1, n2)

if fim - inicio <= 1:
    print("Não há números inteiros no intervalo.")
else:
    print(f"Números inteiros entre {inicio} e {fim}:")
    for n in range(inicio + 1, fim):
        print(n)
