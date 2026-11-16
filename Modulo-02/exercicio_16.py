# Esse exercício me ajudou a fixar a lógica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

# Esse exercÃ­cio me ajudou a fixar a lÃ³gica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

"""
MÃ³dulo 02 - Estruturas Condicionais
ExercÃ­cio 16 - Positivo, negativo ou zero

Enunciado:
Leia um nÃºmero real e informe se ele Ã© positivo, negativo ou igual a zero.

Regra:
Um nÃºmero Ã© positivo se for maior que zero, negativo se for menor que
zero, e zero apenas quando for exatamente igual a zero.
"""


def ler_float(mensagem):
    """LÃª um nÃºmero real aceitando vÃ­rgula ou ponto como separador decimal."""
    texto = input(mensagem).strip().replace(",", ".")
    return float(texto)


numero = ler_float("Digite um nÃºmero: ")

if numero > 0:
    resultado = "POSITIVO"
elif numero < 0:
    resultado = "NEGATIVO"
else:
    resultado = "ZERO"

print(f"\nResultado: {resultado}")

# Teste seu programa (valores da apostila):
# 12    -> POSITIVO
# -0,5  -> NEGATIVO
# 0     -> ZERO

