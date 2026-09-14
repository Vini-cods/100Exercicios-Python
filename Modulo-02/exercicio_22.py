"""
Módulo 02 - Estruturas Condicionais
Exercício 22 - Situação do aluno por faixa

Enunciado:
Leia duas notas, calcule a média e informe a situação do aluno
conforme a tabela.

Regras do exercício:
Média < 5,0                     -> REPROVADO
Média >= 5,0 e < 7,0             -> RECUPERAÇÃO
Média >= 7,0                     -> APROVADO
"""


def ler_float(mensagem):
    texto = input(mensagem).strip().replace(",", ".")
    return float(texto)


def formatar(valor, casas=1):
    return f"{valor:.{casas}f}".replace(".", ",")


nota1 = ler_float("Nota 1: ")
nota2 = ler_float("Nota 2: ")

media = (nota1 + nota2) / 2

if media < 5:
    situacao = "REPROVADO"
elif media < 7:
    situacao = "RECUPERAÇÃO"
else:
    situacao = "APROVADO"

print(f"\nMédia: {formatar(media)}")
print(f"Situação: {situacao}")

# Teste seu programa (valores da apostila):
# 4,0 e 5,0 -> Média 4,5 -> REPROVADO
# 5,0 e 5,0 -> Média 5,0 -> RECUPERAÇÃO
# 7,0 e 7,0 -> Média 7,0 -> APROVADO
