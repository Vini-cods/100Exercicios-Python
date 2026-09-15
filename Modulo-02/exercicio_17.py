# Esse exercício me ajudou a fixar a lógica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

# Esse exercÃ­cio me ajudou a fixar a lÃ³gica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

"""
MÃ³dulo 02 - Estruturas Condicionais
ExercÃ­cio 17 - Par ou Ã­mpar

Enunciado:
Leia um nÃºmero inteiro e informe se ele Ã© par ou Ã­mpar.

Regra:
Um nÃºmero Ã© par quando o resto da divisÃ£o por 2 Ã© igual a zero.
(Isso vale tambÃ©m para nÃºmeros negativos: -8 % 2 == 0.)
"""

numero = int(input("Digite um nÃºmero: "))

if numero % 2 == 0:
    resultado = "PAR"
else:
    resultado = "ÃMPAR"

print(f"\nResultado: {resultado}")

# Teste seu programa (valores da apostila):
# 13  -> ÃMPAR
# 0   -> PAR
# -8  -> PAR

