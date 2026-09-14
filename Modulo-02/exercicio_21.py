"""
Módulo 02 - Estruturas Condicionais
Exercício 21 - Aprovado ou reprovado

Enunciado:
Leia duas notas, calcule a média e informe se o aluno foi aprovado
ou reprovado.

Regra:
Média maior ou igual a 7,0 significa APROVADO.
Abaixo de 7,0 significa REPROVADO.
"""


def ler_float(mensagem):
    texto = input(mensagem).strip().replace(",", ".")
    return float(texto)


def formatar(valor, casas=1):
    return f"{valor:.{casas}f}".replace(".", ",")


nota1 = ler_float("Nota 1: ")
nota2 = ler_float("Nota 2: ")

media = (nota1 + nota2) / 2

if media >= 7:
    situacao = "APROVADO"
else:
    situacao = "REPROVADO"

print(f"\nMédia: {formatar(media)}")
print(f"Situação: {situacao}")

# Teste seu programa (valores da apostila):
# 5,0 e 8,0  -> Média 6,5 -> REPROVADO
# 7,0 e 7,0  -> Média 7,0 -> APROVADO
# 10,0 e 9,0 -> Média 9,5 -> APROVADO
