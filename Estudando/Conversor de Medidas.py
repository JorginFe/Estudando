def metros_para_quilometros(metros):
    return metros / 1000

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    print("Conversor de Unidades")
    escolha = input("Escolha a opção (1 para metros para quilômetros, 2 para Celsius para Fahrenheit): ")

    if escolha == "1":
        metros = float(input("Digite a distância em metros: "))
        resultado = metros_para_quilometros(metros)
        print(f"{metros} metros é igual a {resultado:.2f} quilômetros.")
    
    elif escolha == "2":
        celsius = float(input("Digite a temperatura em Celsius: "))
        resultado = celsius_para_fahrenheit(celsius)
        print(f"{celsius} graus Celsius é igual a {resultado:.2f} graus Fahrenheit.")
    
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")

if __name__ == "__main__":
    main()