contador = 1

try:
    numero = int(input("Digite o numero desejado: "))
except ValueError:
        print("Valor digitado incorretamente, tente novamente.")

while contador <= 10:
    resultado = contador * numero
    print(f"{contador} x {numero} = {resultado}")
    contador += 1