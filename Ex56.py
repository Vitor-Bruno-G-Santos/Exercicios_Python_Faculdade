livros = int(input("Informe a quantidade de livros comprados no bimestre: "))

if livros <= 0:
    pontos = 0
elif livros == 1:
    pontos = 5
elif livros == 2:
    pontos = 15
elif livros == 3:
    pontos = 30
else:
    pontos = 60

print(f"Pontuação acumulada: {pontos} pontos")

if 20 <= pontos <= 30:
    print("Brinde: Uma Eco Bag OU Caneta personalizada")
elif 35 <= pontos <= 60:
    print("Brinde: Um livro (com valor máximo de R$ 30,00) OU Luminária de cabeceira")
elif pontos > 65:
    print("Brinde: 2 livros (com valor máximo de R$ 100,00) OU Power bank")
else:
    print("Pontuação insuficiente para resgatar brindes.")
