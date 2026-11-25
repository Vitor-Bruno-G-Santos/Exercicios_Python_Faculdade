numero = int(input("Informe um número inteiro entre 1 e 10 para ver a tabuada: "))

if 1 <= numero <= 10:
    print(f"Tabuada de {numero}:")
    for i in range(1, 11):
        print(f"{numero} X {i} = {numero * i}")
else:
    print("Número inválido! Digite um valor entre 1 e 10.")
