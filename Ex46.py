nome = input("Informe o nome: ")
sexo = input("Informe o sexo (M/F): ").strip().upper()
estado_civil = input("Informe o estado civil: ").strip().upper()

tempo_casada = None
if sexo == "F" and estado_civil == "CASADA":
    tempo_casada = int(input("Informe o tempo de casada (em anos): "))

print(f"\nNome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado civil: {estado_civil}")
if tempo_casada:
    print(f"Tempo de casada: {tempo_casada} anos")
