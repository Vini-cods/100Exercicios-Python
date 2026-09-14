"""
Módulo 02 - Estruturas Condicionais
Exercício 20 - Três valores em ordem crescente

Enunciado:
Leia três números inteiros e mostre os valores em ordem crescente.

Requisito:
Aceite valores repetidos.
"""

entrada = input("Valores (separados por vírgula): ")
valores = [int(v.strip()) for v in entrada.split(",")]

crescente = sorted(valores)

print(f"\nOrdem crescente: {crescente[0]}, {crescente[1]}, {crescente[2]}")

# Teste seu programa (valores da apostila):
# 3, 1, 2   -> 1, 2, 3
# 7, 7, 4   -> 4, 7, 7
# -1, -5, 0 -> -5, -1, 0
