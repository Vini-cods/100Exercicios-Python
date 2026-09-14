"""
Módulo 02 - Estruturas Condicionais
Exercício 29 - Tipo de triângulo

Enunciado:
Leia três medidas. Primeiro verifique se elas formam um triângulo.
Se formarem, classifique-o como equilátero, isósceles ou escaleno.

Regras do exercício:
Três lados iguais    -> EQUILÁTERO
Dois lados iguais    -> ISÓSCELES
Três lados diferentes -> ESCALENO
"""


def ler_float(mensagem):
    texto = input(mensagem).strip().replace(",", ".")
    return float(texto)


a = ler_float("Lado 1: ")
b = ler_float("Lado 2: ")
c = ler_float("Lado 3: ")

if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        tipo = "EQUILÁTERO"
    elif a == b or b == c or a == c:
        tipo = "ISÓSCELES"
    else:
        tipo = "ESCALENO"
else:
    tipo = "NÃO FORMA TRIÂNGULO"

print(f"\nResultado: {tipo}")

# Teste seu programa (valores da apostila):
# 5, 5, 5 -> EQUILÁTERO
# 5, 5, 3 -> ISÓSCELES
# 3, 4, 5 -> ESCALENO
# 1, 2, 3 -> NÃO FORMA TRIÂNGULO
