"""
Módulo 02 - Estruturas Condicionais
Exercício 24 - Ano bissexto

Enunciado:
Leia um ano inteiro e informe se ele é bissexto.

Regra:
Um ano é bissexto quando é divisível por 400, ou quando é divisível
por 4 e não é divisível por 100.
"""

ano = int(input("Ano: "))

if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    resultado = "BISSEXTO"
else:
    resultado = "NÃO BISSEXTO"

print(f"\nResultado: {resultado}")

# Teste seu programa (valores da apostila):
# 2024 -> BISSEXTO
# 1900 -> NÃO BISSEXTO  (divisível por 100, mas não por 400)
# 2000 -> BISSEXTO      (divisível por 400)
# 2023 -> NÃO BISSEXTO
