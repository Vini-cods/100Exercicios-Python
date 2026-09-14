"""
Módulo 02 - Estruturas Condicionais
Exercício 16 - Positivo, negativo ou zero

Enunciado:
Leia um número real e informe se ele é positivo, negativo ou igual a zero.

Regra:
Um número é positivo se for maior que zero, negativo se for menor que
zero, e zero apenas quando for exatamente igual a zero.
"""


def ler_float(mensagem):
    """Lê um número real aceitando vírgula ou ponto como separador decimal."""
    texto = input(mensagem).strip().replace(",", ".")
    return float(texto)


numero = ler_float("Digite um número: ")

if numero > 0:
    resultado = "POSITIVO"
elif numero < 0:
    resultado = "NEGATIVO"
else:
    resultado = "ZERO"

print(f"\nResultado: {resultado}")

# Teste seu programa (valores da apostila):
# 12    -> POSITIVO
# -0,5  -> NEGATIVO
# 0     -> ZERO
