while True:
    try:
        SANDUICHES = {
            100: {
                "nome": "Cachorro Quente",
                "preco": 11.2
            },
            101: {
                "nome": "Ovo Simples",
                "preco": 8.3
            },  
            102: {
                "nome":"Bauru com Ovo",
                "preco": 11.5
            },  
            103: {
                "nome": "Hamburguer",
                "preco": 16.2
            }
        }
        BEBIDAS = {
            201: {
                "nome": "Refrigerante",
                "preco": 6
            },  
            202: {
                "nome": "Suco",
                "preco": 7.5
            }, 
            203: {
                "nome": "Agua Mineral",
                "preco": 4.7
            }
        }
        for codigo ,sanduiche in SANDUICHES.items():
            print(f"Codigo: {codigo} | {sanduiche["nome"]} - R$ {sanduiche['preco']:.2f}")
        
        for codigo ,bebida in BEBIDAS.items():
            print(f"Codigo: {codigo} | {bebida["nome"]} - R$ {bebida['preco']:.2f}")

        codigo_sanduiche = int(input("Informe o código do sanduíche: "))
        codigo_bebida = int(input("Informe o código da bebida: "))

        total = SANDUICHES[codigo_sanduiche]["preco"] + BEBIDAS[codigo_bebida]["preco"]

        print(f"Valor a pagar: R$ {total:.2f}")
        break
    except:
        print("Codigo do sanduiche ou bebida não encontrado")