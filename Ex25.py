camisetaPequena = int(input("Digite a quantidade de camisetas pequenas: "))
camisetaMedia = int(input("Digite a quantidade de camisetas medias: "))
camisetaGrande = int(input("Digite a quantidade de camisetas grandes: "))

total = (camisetaPequena * 10) + (camisetaMedia * 12) + (camisetaGrande * 15)

print(f"Valor total da compra: R${total}")