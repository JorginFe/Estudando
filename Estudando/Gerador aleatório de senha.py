import secrets
import string

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    tamanho_senha = int(input("Quantos caracteres você deseja ter em sua senha?"))
    senha_gerada = gerar_senha(tamanho_senha)
    print(f"Sua senha gerada é: {senha_gerada}")

if __name__ == "__main__":
    main()