lado1 = float(input("Digite o primeiro lado do triangulo: "))
lado2 = float(input("Digite o segundo lado do triangulo: "))
lado3 = float(input("Digite o terceiro lado do triangulo: "))

if(lado1 == lado2 and lado2 == lado3 and lado1 == lado3):
    print("Triangulo equilatero")
elif(lado1 == lado2 or lado2 == lado3 or lado3 == lado1):
    print("Triagulo isoceles")
else:
    print("Triangulo escaleno")