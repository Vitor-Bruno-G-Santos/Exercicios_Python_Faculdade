valorProduto = float(input("Digite o valor pago no produto: "))

print(f"Valor venda: R${valorProduto * 1.45}") if valorProduto < 50 else print(f"Valor venda: R${valorProduto * 1.30}")