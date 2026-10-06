while True:
    try:
        SANDUICHES = {
            100: 11.20,  # Cachorro Quente
            101: 8.30,   # Ovo Simples
            102: 11.50,  # Bauru com Ovo
            103: 16.20,  # Hambúrguer
        }
        BEBIDAS = {
            201: 6.00,   # Refrigerante
            202: 7.50,   # Suco
            203: 4.70,   # Água Mineral
        }

        codigo_sanduiche = int(input("Informe o código do sanduíche: "))
        codigo_bebida = int(input("Informe o código da bebida: "))

        total = SANDUICHES[codigo_sanduiche] + BEBIDAS[codigo_bebida]

        print(f"Valor a pagar: R$ {total:.2f}")
        break
    except:
        print("Codigo do sanduiche ou bebida não encontrado")