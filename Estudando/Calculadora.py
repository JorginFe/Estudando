def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y != 0:
        return x / y
        return round(resultado, 1)
    else:
        return "Não se pode dividir um número por zero"

while True:
    try:
        num1 = float(input("Digite um número: "))
        num2 = float(input("Digite outro número: "))
        break
    except ValueError:
        print("Utilize apenas números.")

print("Escolha a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

while True:
    escolha = input("Digite a opção (1/2/3/4): ")

    if escolha in ('1', '2', '3', '4'):
        escolha = int(escolha)
        break
    else:
        print("Opção inválida. Tente novamente.")

if escolha == 1:
    print(num1, "+", num2, "=", adicao(num1, num2))
elif escolha == 2:
    print(num1, "-", num2, "=", subtracao(num1, num2))
elif escolha == 3:
    print(num1, "*", num2, "=", multiplicacao(num1, num2))
elif escolha == 4:
    print(num1, "/", num2, "=", divisao(num1, num2))