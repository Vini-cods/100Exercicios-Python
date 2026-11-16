# Esse exercício me ajudou a fixar a lógica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

# Esse exercÃ­cio me ajudou a fixar a lÃ³gica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

"""
MÃ³dulo 02 - Estruturas Condicionais
ExercÃ­cio 33 - Dia da semana

Enunciado:
Leia um nÃºmero de 1 a 7 e mostre o dia da semana correspondente.
Para qualquer outro valor, mostre OPÃ‡ÃƒO INVÃLIDA.

Tabela de referÃªncia:
1 -> SEGUNDA-FEIRA   5 -> SEXTA-FEIRA
2 -> TERÃ‡A-FEIRA     6 -> SÃBADO
3 -> QUARTA-FEIRA    7 -> DOMINGO
4 -> QUINTA-FEIRA
"""

numero = int(input("Digite um nÃºmero (1 a 7): "))

dias_da_semana = {
    1: "SEGUNDA-FEIRA",
    2: "TERÃ‡A-FEIRA",
    3: "QUARTA-FEIRA",
    4: "QUINTA-FEIRA",
    5: "SEXTA-FEIRA",
    6: "SÃBADO",
    7: "DOMINGO",
}

resultado = dias_da_semana.get(numero, "OPÃ‡ÃƒO INVÃLIDA")

print(f"\nResultado: {resultado}")

# Teste seu programa (valores da apostila):
# 1 -> SEGUNDA-FEIRA
# 6 -> SÃBADO
# 7 -> DOMINGO
# 9 -> OPÃ‡ÃƒO INVÃLIDA (teste tambÃ©m com 0 e 8)

