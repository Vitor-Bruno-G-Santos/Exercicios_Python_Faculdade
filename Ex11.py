nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade"))

if(idade >= 0 and idade <= 2):
    print(f"{nome} está com {idade} e pela tabela é considerado um bebê")
elif(idade <= 11):
    print(f"{nome} está com {idade} e pela tabela é considerado uma criança")
elif(idade <= 21):
    print(f"{nome} está com {idade} e pela tabela é considerado um jovem")
elif(idade <= 64):
    print(f"{nome} está com {idade} e pela tabela é considerado um adulto")
elif(idade <= 100):
    print(f"{nome} está com {idade} e pela tabela é considerado um idoso")
elif(idade >= 101):
    print(f"{nome} está com {idade} e pela tabela é considerado um velinho")
else:
    print("Idade invalida")


