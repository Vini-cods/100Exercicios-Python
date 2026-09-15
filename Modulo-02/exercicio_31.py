# Esse exercício me ajudou a fixar a lógica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

# Esse exercÃ­cio me ajudou a fixar a lÃ³gica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

"""
MÃ³dulo 02 - Estruturas Condicionais
ExercÃ­cio 31 - DivisÃ­vel por 3 e por 5

Enunciado:
Leia um nÃºmero inteiro e informe em qual situaÃ§Ã£o ele se encontra.

Regras do exercÃ­cio:
DivisÃ­vel por 3 e por 5 -> DIVISÃVEL POR 3 E 5
Apenas por 3            -> DIVISÃVEL APENAS POR 3
Apenas por 5            -> DIVISÃVEL APENAS POR 5
Por nenhum dos dois     -> NÃƒO DIVISÃVEL POR 3 NEM 5
"""

numero = int(input("Digite um nÃºmero: "))

div3 = numero % 3 == 0
div5 = numero % 5 == 0

if div3 and div5:
    resultado = "DIVISÃVEL POR 3 E 5"
elif div3:
    resultado = "DIVISÃVEL APENAS POR 3"
elif div5:
    resultado = "DIVISÃVEL APENAS POR 5"
else:
    resultado = "NÃƒO DIVISÃVEL POR 3 NEM 5"

print(f"\nResultado: {resultado}")

# Teste seu programa (valores da apostila):
# 30 -> DIVISÃVEL POR 3 E 5
# 9  -> DIVISÃVEL APENAS POR 3
# 20 -> DIVISÃVEL APENAS POR 5
# 7  -> NÃƒO DIVISÃVEL POR 3 NEM 5

