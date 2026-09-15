# Esse exercício me ajudou a fixar a lógica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

# Esse exercÃ­cio me ajudou a fixar a lÃ³gica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

"""
MÃ³dulo 02 - Estruturas Condicionais
ExercÃ­cio 32 - NÃºmero dentro do intervalo

Enunciado:
Leia um nÃºmero real e informe se ele estÃ¡ dentro do intervalo fechado
de 10 atÃ© 20.

Regra:
Os valores 10 e 20 pertencem ao intervalo (intervalo fechado).
"""


def ler_float(mensagem):
    texto = input(mensagem).strip().replace(",", ".")
    return float(texto)


numero = ler_float("Digite um nÃºmero: ")

if 10 <= numero <= 20:
    resultado = "DENTRO"
else:
    resultado = "FORA"

print(f"\nResultado: {resultado}")

# Teste seu programa (valores da apostila):
# 10   -> DENTRO
# 15,5 -> DENTRO
# 20   -> DENTRO
# 20,1 -> FORA

