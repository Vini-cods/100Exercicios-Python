# Esse exercício me ajudou a fixar a lógica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

# Esse exercÃ­cio me ajudou a fixar a lÃ³gica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

"""
MÃ³dulo 02 - Estruturas Condicionais
ExercÃ­cio 20 - TrÃªs valores em ordem crescente

Enunciado:
Leia trÃªs nÃºmeros inteiros e mostre os valores em ordem crescente.

Requisito:
Aceite valores repetidos.
"""

entrada = input("Valores (separados por vÃ­rgula): ")
valores = [int(v.strip()) for v in entrada.split(",")]

crescente = sorted(valores)

print(f"\nOrdem crescente: {crescente[0]}, {crescente[1]}, {crescente[2]}")

# Teste seu programa (valores da apostila):
# 3, 1, 2   -> 1, 2, 3
# 7, 7, 4   -> 4, 7, 7
# -1, -5, 0 -> -5, -1, 0

