soma = 0
numero = None

while numero != 0:
    try:
        numero = int(input("Digite o numero desejado: "))
        soma += numero
        
    except ValueError:
        print("Valor digitado incorretamente, tente novamente.")

print(soma)