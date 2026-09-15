# Esse exercício me ajudou a fixar a lógica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

# Esse exercÃ­cio me ajudou a fixar a lÃ³gica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

"""
MÃ³dulo 02 - Estruturas Condicionais
ExercÃ­cio 22 - SituaÃ§Ã£o do aluno por faixa

Enunciado:
Leia duas notas, calcule a mÃ©dia e informe a situaÃ§Ã£o do aluno
conforme a tabela.

Regras do exercÃ­cio:
MÃ©dia < 5,0                     -> REPROVADO
MÃ©dia >= 5,0 e < 7,0             -> RECUPERAÃ‡ÃƒO
MÃ©dia >= 7,0                     -> APROVADO
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
    situacao = "RECUPERAÃ‡ÃƒO"
else:
    situacao = "APROVADO"

print(f"\nMÃ©dia: {formatar(media)}")
print(f"SituaÃ§Ã£o: {situacao}")

# Teste seu programa (valores da apostila):
# 4,0 e 5,0 -> MÃ©dia 4,5 -> REPROVADO
# 5,0 e 5,0 -> MÃ©dia 5,0 -> RECUPERAÃ‡ÃƒO
# 7,0 e 7,0 -> MÃ©dia 7,0 -> APROVADO

