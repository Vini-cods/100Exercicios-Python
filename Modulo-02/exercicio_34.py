"""
Módulo 02 - Estruturas Condicionais
Exercício 34 - Quantidade de dias do mês

Enunciado:
Leia o número de um mês e um ano. Mostre quantos dias o mês possui.

Regra:
Meses 1, 3, 5, 7, 8, 10 e 12 possuem 31 dias.
Meses 4, 6, 9 e 11 possuem 30 dias.
Fevereiro possui 28 dias, ou 29 em ano bissexto.

Requisito:
Se o mês estiver fora de 1 a 12, mostre MÊS INVÁLIDO.
"""

mes = int(input("Mês: "))
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
    print("\nResultado: MÊS INVÁLIDO")
else:
    print(f"\nResultado: {dias} dias")

# Teste seu programa (valores da apostila):
# Mês 2,  Ano 2024 -> 29 dias
# Mês 2,  Ano 2023 -> 28 dias
# Mês 4,  Ano 2026 -> 30 dias
# Mês 12, Ano 2026 -> 31 dias
# Mês 13, Ano 2026 -> MÊS INVÁLIDO
