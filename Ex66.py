pop_a = 80000
pop_b = 200000
taxa_a = 0.03
taxa_b = 0.015
anos = 0

while pop_a < pop_b:
    pop_a += pop_a * taxa_a
    pop_b += pop_b * taxa_b
    anos += 1

print(f"Serão necessários {anos} anos para a população do país A ultrapassar ou igualar a do país B.")
print(f"População final de A: {pop_a:.0f}")
print(f"População final de B: {pop_b:.0f}")
