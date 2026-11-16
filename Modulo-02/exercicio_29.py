# Esse exercício me ajudou a fixar a lógica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

# Esse exercÃ­cio me ajudou a fixar a lÃ³gica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

"""
MÃ³dulo 02 - Estruturas Condicionais
ExercÃ­cio 29 - Tipo de triÃ¢ngulo

Enunciado:
Leia trÃªs medidas. Primeiro verifique se elas formam um triÃ¢ngulo.
Se formarem, classifique-o como equilÃ¡tero, isÃ³sceles ou escaleno.

Regras do exercÃ­cio:
TrÃªs lados iguais    -> EQUILÃTERO
Dois lados iguais    -> ISÃ“SCELES
TrÃªs lados diferentes -> ESCALENO
"""


def ler_float(mensagem):
    texto = input(mensagem).strip().replace(",", ".")
    return float(texto)


a = ler_float("Lado 1: ")
b = ler_float("Lado 2: ")
c = ler_float("Lado 3: ")

if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        tipo = "EQUILÃTERO"
    elif a == b or b == c or a == c:
        tipo = "ISÃ“SCELES"
    else:
        tipo = "ESCALENO"
else:
    tipo = "NÃƒO FORMA TRIÃ‚NGULO"

print(f"\nResultado: {tipo}")

# Teste seu programa (valores da apostila):
# 5, 5, 5 -> EQUILÃTERO
# 5, 5, 3 -> ISÃ“SCELES
# 3, 4, 5 -> ESCALENO
# 1, 2, 3 -> NÃƒO FORMA TRIÃ‚NGULO

