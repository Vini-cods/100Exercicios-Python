# Esse exercício me ajudou a fixar a lógica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

# Esse exercÃ­cio me ajudou a fixar a lÃ³gica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

"""
MÃ³dulo 02 - Estruturas Condicionais
ExercÃ­cio 28 - Ã‰ possÃ­vel formar um triÃ¢ngulo?

Enunciado:
Leia trÃªs medidas positivas e informe se elas podem formar um
triÃ¢ngulo.

Regra:
TrÃªs lados formam um triÃ¢ngulo quando cada lado Ã© menor que a soma
dos outros dois.
"""


def ler_float(mensagem):
    texto = input(mensagem).strip().replace(",", ".")
    return float(texto)


a = ler_float("Lado 1: ")
b = ler_float("Lado 2: ")
c = ler_float("Lado 3: ")

if a < b + c and b < a + c and c < a + b:
    resultado = "FORMAM UM TRIÃ‚NGULO"
else:
    resultado = "NÃƒO FORMAM UM TRIÃ‚NGULO"

print(f"\nResultado: {resultado}")

# Teste seu programa (valores da apostila):
# 2, 2, 3  -> FORMAM
# 1, 2, 3  -> NÃƒO FORMAM
# 5, 5, 10 -> NÃƒO FORMAM

