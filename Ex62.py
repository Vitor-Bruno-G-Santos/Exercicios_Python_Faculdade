numero = int(input("Digite um número inteiro para calcular o fatorial: "))

if numero < 0:
    print("Não existe fatorial de número negativo.")
elif numero == 0:
    print("0!=1")
else:
    fatorial = 1
    termos = []
    for i in range(numero, 0, -1):
        fatorial *= i
        termos.append(str(i))
    expressao = ".".join(termos)
    print(f"{numero}!={expressao}={fatorial}")
