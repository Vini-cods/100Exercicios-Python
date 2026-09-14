"""
Módulo 02 - Estruturas Condicionais
Exercício 32 - Número dentro do intervalo

Enunciado:
Leia um número real e informe se ele está dentro do intervalo fechado
de 10 até 20.

Regra:
Os valores 10 e 20 pertencem ao intervalo (intervalo fechado).
"""


def ler_float(mensagem):
    texto = input(mensagem).strip().replace(",", ".")
    return float(texto)


numero = ler_float("Digite um número: ")

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
