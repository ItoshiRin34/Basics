import secrets
import string

def gerador(tamanho=20):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
    return senha

print(gerador(600))