aluno = input("Digite o nome do aluno: ")
disciplina = input("Digite o nome da disciplina: ")
nota1 = float(input(f"Digite a primeira nota do {aluno}: "))
nota2 = float(input(f"Digite a segunda nota do {aluno}: "))
nota3 = float(input(f"Digite a terceira nota do {aluno}: "))

media = (nota1 + nota2 + nota3) / 3
aprovado = "Aprovado" if media >= 6 else "Reprovado"

print("_____NOTAS_____")
print("Aluno:", aluno)
print("Disciplina:", disciplina)
print("Nota 1:", nota1)
print("Nota 2:", nota2)
print("Nota 3:", nota3)
print("Média:", media)
print("Status:", aprovado)


