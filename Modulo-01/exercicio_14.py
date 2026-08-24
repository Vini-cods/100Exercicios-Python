# Exercício 14 - Troca de valores
#
# Objetivo: trocar o valor de A com o valor de B, usando uma variável auxiliar.
# Sem essa variável auxiliar, ao fazer "A = B" perderíamos o valor original de A.

A = float(input("Leia A: "))
B = float(input("Leia B: "))

auxiliar = A
A = B
B = auxiliar

print(f"A depois da troca: {A}")
print(f"B depois da troca: {B}")
