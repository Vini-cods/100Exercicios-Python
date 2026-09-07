"""
MÓDULO 02 - ESTRUTURAS CONDICIONAIS                          EXERCÍCIO 10

MAIOR ENTRE DOIS NÚMEROS

Enunciado:
    Leia dois números inteiros e informe qual deles é o maior. Caso
    os dois valores sejam iguais, informe que são iguais.

Exemplo de execução:
    Primeiro valor: 8
    Segundo valor: 5
    Maior valor: 8

Teste seu programa:
    Valor 1  Valor 2  ->  Resultado esperado
    8        5        ->  Maior valor: 8
    3        3        ->  Os dois valores são iguais.
    2        9        ->  Maior valor: 9

Verificação final:
    Teste um caso em que os dois valores informados sejam iguais e
    confirme que o programa não aponta nenhum dos dois como maior.
"""

valor1 = int(input("Primeiro valor: "))
valor2 = int(input("Segundo valor: "))

if valor1 > valor2:
    print(f"Maior valor: {valor1}")
elif valor2 > valor1:
    print(f"Maior valor: {valor2}")
else:
    print("Os dois valores são iguais.")
