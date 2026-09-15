# Esse exercício me ajudou a fixar a lógica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

# Esse exercÃ­cio me ajudou a fixar a lÃ³gica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

"""
MÃ³dulo 02 - Estruturas Condicionais
ExercÃ­cio 24 - Ano bissexto

Enunciado:
Leia um ano inteiro e informe se ele Ã© bissexto.

Regra:
Um ano Ã© bissexto quando Ã© divisÃ­vel por 400, ou quando Ã© divisÃ­vel
por 4 e nÃ£o Ã© divisÃ­vel por 100.
"""

ano = int(input("Ano: "))

if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    resultado = "BISSEXTO"
else:
    resultado = "NÃƒO BISSEXTO"

print(f"\nResultado: {resultado}")

# Teste seu programa (valores da apostila):
# 2024 -> BISSEXTO
# 1900 -> NÃƒO BISSEXTO  (divisÃ­vel por 100, mas nÃ£o por 400)
# 2000 -> BISSEXTO      (divisÃ­vel por 400)
# 2023 -> NÃƒO BISSEXTO

