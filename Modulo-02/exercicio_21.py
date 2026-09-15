# Esse exercício me ajudou a fixar a lógica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

# Esse exercÃ­cio me ajudou a fixar a lÃ³gica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

"""
MÃ³dulo 02 - Estruturas Condicionais
ExercÃ­cio 21 - Aprovado ou reprovado

Enunciado:
Leia duas notas, calcule a mÃ©dia e informe se o aluno foi aprovado
ou reprovado.

Regra:
MÃ©dia maior ou igual a 7,0 significa APROVADO.
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

print(f"\nMÃ©dia: {formatar(media)}")
print(f"SituaÃ§Ã£o: {situacao}")

# Teste seu programa (valores da apostila):
# 5,0 e 8,0  -> MÃ©dia 6,5 -> REPROVADO
# 7,0 e 7,0  -> MÃ©dia 7,0 -> APROVADO
# 10,0 e 9,0 -> MÃ©dia 9,5 -> APROVADO

