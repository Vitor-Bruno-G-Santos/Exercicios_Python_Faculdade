maior_acidentes = None
cidade_maior = None
menor_acidentes = None
cidade_menor = None

total_veiculos = 0
acidentes_menos_2000 = 0
qtd_cidades_menos_2000 = 0

for i in range(1, 6):
    print(f"\n--- Cidade {i} ---")
    codigo = input("Código da cidade: ")
    veiculos = int(input("Número de veículos de passeio (1999): "))
    acidentes = int(input("Número de acidentes de trânsito com vítimas (1999): "))

    if maior_acidentes is None or acidentes > maior_acidentes:
        maior_acidentes = acidentes
        cidade_maior = codigo
    if menor_acidentes is None or acidentes < menor_acidentes:
        menor_acidentes = acidentes
        cidade_menor = codigo

    total_veiculos += veiculos

    if veiculos < 2000:
        acidentes_menos_2000 += acidentes
        qtd_cidades_menos_2000 += 1

media_veiculos = total_veiculos / 5

print("\n=== RESULTADOS ===")
print(f"Maior índice de acidentes: {maior_acidentes} (Cidade {cidade_maior})")
print(f"Menor índice de acidentes: {menor_acidentes} (Cidade {cidade_menor})")
print(f"Média de veículos nas cinco cidades: {media_veiculos:.2f}")

if qtd_cidades_menos_2000 > 0:
    media_acidentes_menos_2000 = acidentes_menos_2000 / qtd_cidades_menos_2000
    print(f"Média de acidentes em cidades com menos de 2.000 veículos: {media_acidentes_menos_2000:.2f}")
else:
    print("Nenhuma cidade possui menos de 2.000 veículos de passeio.")
