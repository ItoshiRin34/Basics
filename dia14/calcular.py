import sys

# Verificar se foram passados exatamente 3 números
if len(sys.argv) != 4:
    print("Uso: python calcular.py <numero1> <numero2> <numero3>")
    sys.exit(1)

try:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    num3 = float(sys.argv[3])
except ValueError:
    print("Erro: todos os argumentos precisam ser números.")
    sys.exit(1)

# Evitar divisão por zero
if num2 == 0 or num3 == 0:
    print("Erro: divisão por zero não é permitida.")
    sys.exit(1)

# Cálculos
soma = num1 + num2 + num3
produto = num1 * num2 * num3
divisao = num1 / (num2 * num3)
subtracao = num1 - num2 - num3

# Resultado
print(
    f"Soma: {soma} | "
    f"Produto: {produto} | "
    f"Divisão: {divisao} | "
    f"Subtração: {subtracao}"
)
