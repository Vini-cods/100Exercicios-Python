# Exercício 02 - Média de duas notas
#
# Regra: Média = (nota 1 + nota 2) / 2
# O resultado deve ser mostrado com uma casa decimal.

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1 + nota2) / 2

# ":.1f" formata o número com apenas uma casa decimal
print(f"Média: {media:.1f}")
