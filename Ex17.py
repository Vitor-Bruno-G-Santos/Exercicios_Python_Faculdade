salario = float(input("Digite o valor do seu salario: "))
print(f"Salario antes do reajuste: {salario}")

if salario <= 280:
    print("Percentual: 20%")
    print(f"Valor do aumento: R${salario * 0.20}")
    salario *= 1.2
elif salario <= 700:
    print("Percentual: 15%")
    print(f"Valor do aumento: R${salario * 0.15}")
    salario *= 1.15
elif salario <= 1500:
    print("Percentual: 10%")
    print(f"Valor do aumento: R${salario * 0.1}")
    salario *= 1.1
else: 
    print("Percentual: 5%")
    print(f"Valor do aumento: R${salario * 0.05}")
    salario *= 1.05

print(f"Salario após o reajuste {salario}")