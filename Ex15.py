sexo = input("Digite seu sexo(M ou F): ")
sexo = sexo.upper()

print("Masculino") if sexo == "M" else print("Sexo invalido") if sexo != "F" else print("Feminino")