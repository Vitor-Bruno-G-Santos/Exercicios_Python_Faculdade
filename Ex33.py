num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Operações: + (soma), - (subtração), * (multiplicação), / (divisão)")
operacao = input("Qual operação deseja realizar? ").strip()

valido = True

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 == 0:
        print("Erro: divisão por zero!")
        valido = False
    else:
        resultado = num1 / num2
else:
    print("Operação inválida!")
    valido = False

if valido:
    if resultado.is_integer():
        print(f"Resultado: {int(resultado)}")
        print("O número é inteiro.")
        if resultado % 2 == 0:
            print("O número é par.")
        else:
            print("O número é ímpar.")
    else:
        print(f"Resultado: {resultado}")
        print("O número é decimal.")
        print("Par ou ímpar não se aplica a números decimais.")

    if resultado > 0:
        print("O número é positivo.")
    elif resultado < 0:
        print("O número é negativo.")
    else:
        print("O número é zero (nem positivo nem negativo).")