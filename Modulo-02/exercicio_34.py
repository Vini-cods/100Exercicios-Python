# Esse exercício me ajudou a fixar a lógica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

# Esse exercÃ­cio me ajudou a fixar a lÃ³gica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

"""
MÃ³dulo 02 - Estruturas Condicionais
ExercÃ­cio 34 - Quantidade de dias do mÃªs

Enunciado:
Leia o nÃºmero de um mÃªs e um ano. Mostre quantos dias o mÃªs possui.

Regra:
Meses 1, 3, 5, 7, 8, 10 e 12 possuem 31 dias.
Meses 4, 6, 9 e 11 possuem 30 dias.
Fevereiro possui 28 dias, ou 29 em ano bissexto.

Requisito:
Se o mÃªs estiver fora de 1 a 12, mostre MÃŠS INVÃLIDO.
"""

mes = int(input("MÃªs: "))
ano = int(input("Ano: "))

meses_31_dias = (1, 3, 5, 7, 8, 10, 12)
meses_30_dias = (4, 6, 9, 11)

if mes in meses_31_dias:
    dias = 31
elif mes in meses_30_dias:
    dias = 30
elif mes == 2:
    bissexto = (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)
    dias = 29 if bissexto else 28
else:
    dias = None

if dias is None:
    print("\nResultado: MÃŠS INVÃLIDO")
else:
    print(f"\nResultado: {dias} dias")

# Teste seu programa (valores da apostila):
# MÃªs 2,  Ano 2024 -> 29 dias
# MÃªs 2,  Ano 2023 -> 28 dias
# MÃªs 4,  Ano 2026 -> 30 dias
# MÃªs 12, Ano 2026 -> 31 dias
# MÃªs 13, Ano 2026 -> MÃŠS INVÃLIDO

