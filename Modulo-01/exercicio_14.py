# Esse exercício me ajudou a fixar a lógica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

# Esse exercÃ­cio me ajudou a fixar a lÃ³gica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

# ExercÃ­cio 14 - Troca de valores
#
# Objetivo: trocar o valor de A com o valor de B, usando uma variÃ¡vel auxiliar.
# Sem essa variÃ¡vel auxiliar, ao fazer "A = B" perderÃ­amos o valor original de A.

A = float(input("Leia A: "))
B = float(input("Leia B: "))

auxiliar = A
A = B
B = auxiliar

print(f"A depois da troca: {A}")
print(f"B depois da troca: {B}")

