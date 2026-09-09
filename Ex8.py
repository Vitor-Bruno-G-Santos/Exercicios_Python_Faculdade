distancia = int(input("Digite em quilometros a distancia da viagem: "))
valorGasolina = float(input("Digite o preço da gasolina: "))
autonomia = float(input("Digite a média de consumo do seu carro na rodovia: "))

print(f"Custo estimado da viagem: R${(autonomia / distancia) * valorGasolina}")