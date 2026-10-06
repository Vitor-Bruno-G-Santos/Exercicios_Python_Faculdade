dia = int(input("Informe o dia: "))
mes = int(input("Informe o mês: "))

if mes < 1 or mes > 12 or dia < 1 or dia > 30:
    print("Data inválida!")
else:
    dias_passados = (mes - 1) * 30 + dia
    print(f"Dias desde o início do ano: {dias_passados}")