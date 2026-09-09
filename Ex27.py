for i in range(50):
    matricula = int(input("Digite o numero de matricula: "))
    sexo = input("Digite o sexo (M ou F): ")
    altura = int(input("Digite a sua altura em cm: "))
    statusFisico = int(input("Digite o status fisico (1–bom, 2–regular, 3–ruim): "))
femininoAlto = 0
masculinoBom = 0
masculino = 0
if sexo.upper() == "F" and altura > 170:
    femininoAlto += 1 
if sexo.upper() == "M":
    masculino += 1
    if statusFisico == 1:
        masculinoBom += 1
print(f"Quantidad de alunas com altura superior a 1,70: {femininoAlto}")
print(f"Percentual de alunos com status fisico bom em relação a todos os alunos masculinos: {(masculinoBom / masculino) * 100 }")