"""
Módulo 02 - Estruturas Condicionais
Exercício 33 - Dia da semana

Enunciado:
Leia um número de 1 a 7 e mostre o dia da semana correspondente.
Para qualquer outro valor, mostre OPÇÃO INVÁLIDA.

Tabela de referência:
1 -> SEGUNDA-FEIRA   5 -> SEXTA-FEIRA
2 -> TERÇA-FEIRA     6 -> SÁBADO
3 -> QUARTA-FEIRA    7 -> DOMINGO
4 -> QUINTA-FEIRA
"""

numero = int(input("Digite um número (1 a 7): "))

dias_da_semana = {
    1: "SEGUNDA-FEIRA",
    2: "TERÇA-FEIRA",
    3: "QUARTA-FEIRA",
    4: "QUINTA-FEIRA",
    5: "SEXTA-FEIRA",
    6: "SÁBADO",
    7: "DOMINGO",
}

resultado = dias_da_semana.get(numero, "OPÇÃO INVÁLIDA")

print(f"\nResultado: {resultado}")

# Teste seu programa (valores da apostila):
# 1 -> SEGUNDA-FEIRA
# 6 -> SÁBADO
# 7 -> DOMINGO
# 9 -> OPÇÃO INVÁLIDA (teste também com 0 e 8)
