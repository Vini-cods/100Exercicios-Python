"""
Módulo 02 - Estruturas Condicionais
Exercício 31 - Divisível por 3 e por 5

Enunciado:
Leia um número inteiro e informe em qual situação ele se encontra.

Regras do exercício:
Divisível por 3 e por 5 -> DIVISÍVEL POR 3 E 5
Apenas por 3            -> DIVISÍVEL APENAS POR 3
Apenas por 5            -> DIVISÍVEL APENAS POR 5
Por nenhum dos dois     -> NÃO DIVISÍVEL POR 3 NEM 5
"""

numero = int(input("Digite um número: "))

div3 = numero % 3 == 0
div5 = numero % 5 == 0

if div3 and div5:
    resultado = "DIVISÍVEL POR 3 E 5"
elif div3:
    resultado = "DIVISÍVEL APENAS POR 3"
elif div5:
    resultado = "DIVISÍVEL APENAS POR 5"
else:
    resultado = "NÃO DIVISÍVEL POR 3 NEM 5"

print(f"\nResultado: {resultado}")

# Teste seu programa (valores da apostila):
# 30 -> DIVISÍVEL POR 3 E 5
# 9  -> DIVISÍVEL APENAS POR 3
# 20 -> DIVISÍVEL APENAS POR 5
# 7  -> NÃO DIVISÍVEL POR 3 NEM 5
