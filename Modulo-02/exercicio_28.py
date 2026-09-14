"""
Módulo 02 - Estruturas Condicionais
Exercício 28 - É possível formar um triângulo?

Enunciado:
Leia três medidas positivas e informe se elas podem formar um
triângulo.

Regra:
Três lados formam um triângulo quando cada lado é menor que a soma
dos outros dois.
"""


def ler_float(mensagem):
    texto = input(mensagem).strip().replace(",", ".")
    return float(texto)


a = ler_float("Lado 1: ")
b = ler_float("Lado 2: ")
c = ler_float("Lado 3: ")

if a < b + c and b < a + c and c < a + b:
    resultado = "FORMAM UM TRIÂNGULO"
else:
    resultado = "NÃO FORMAM UM TRIÂNGULO"

print(f"\nResultado: {resultado}")

# Teste seu programa (valores da apostila):
# 2, 2, 3  -> FORMAM
# 1, 2, 3  -> NÃO FORMAM
# 5, 5, 10 -> NÃO FORMAM
