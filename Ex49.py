cotacao = float(input("Informe a cotação do dólar (R$): "))
dolares = float(input("Informe o valor em dólares (US$): "))

reais = dolares * cotacao

print(f"US$ {dolares:.2f} equivalem a R$ {reais:.2f}")
