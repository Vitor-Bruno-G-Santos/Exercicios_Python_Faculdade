vezes_50 = 0

while True:
    numero = int(input("Digite um número inteiro (0 para encerrar): "))
    if numero == 0:
        break
    if numero == 50:
        vezes_50 += 1

print(f"O número 50 foi informado {vezes_50} vez(es).")
