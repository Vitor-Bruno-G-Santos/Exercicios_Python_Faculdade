while True:
    try:
        PRODUTOS = {
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
            },
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
        for codigo ,sanduiche in PRODUTOS.items():
            print(f"Codigo: {codigo} | {sanduiche["nome"]} - R$ {sanduiche['preco']:.2f}")
        pedido = []
        codigo_produto = 1
        while codigo_produto != 0:
            codigo_produto = int(input("Informe o código do produto desejado (0 Para sair): "))
            if codigo_produto != 0: pedido.append(codigo_produto)
        total = 0
        for item in pedido:
            total += PRODUTOS[item]["preco"]

        print(f"Valor a pagar: R$ {total:.2f}")
        break;
    except:
        print("Produto digitado invalido")
