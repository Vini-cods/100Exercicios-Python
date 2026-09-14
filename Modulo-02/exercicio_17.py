"""
Módulo 02 - Estruturas Condicionais
Exercício 17 - Par ou ímpar

Enunciado:
Leia um número inteiro e informe se ele é par ou ímpar.

Regra:
Um número é par quando o resto da divisão por 2 é igual a zero.
(Isso vale também para números negativos: -8 % 2 == 0.)
"""

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    resultado = "PAR"
else:
    resultado = "ÍMPAR"

print(f"\nResultado: {resultado}")

# Teste seu programa (valores da apostila):
# 13  -> ÍMPAR
# 0   -> PAR
# -8  -> PAR
