ano_nascimento = int(input("Informe o ano de nascimento: "))
ano_atual = int(input("Informe o ano atual: "))

anos = ano_atual - ano_nascimento
meses = anos * 12
dias = anos * 365
semanas = anos * 52

print(f"a) Idade em anos: {anos}")
print(f"b) Idade em meses: {meses}")
print(f"c) Idade em dias: {dias}")
print(f"d) Idade em semanas: {semanas}")
