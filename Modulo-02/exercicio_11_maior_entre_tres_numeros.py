"""
MÓDULO 02 - ESTRUTURAS CONDICIONAIS                          EXERCÍCIO 11

MAIOR ENTRE TRÊS NÚMEROS

Enunciado:
    Leia três números inteiros e mostre qual deles é o maior.

Requisito:
    Não utilize a função pronta max(); resolva comparando os valores
    com estruturas condicionais encadeadas.

Exemplo de execução:
    Valor 1: 4
    Valor 2: 9
    Valor 3: 7
    Maior valor: 9

Teste seu programa:
    Valor 1  Valor 2  Valor 3  ->  Resultado esperado
    1        2        3        ->  Maior valor: 3
    10       5        10       ->  Maior valor: 10
    -1       -5       -2       ->  Maior valor: -1

Verificação final:
    Teste um caso em que dois dos três valores sejam iguais e
    correspondam ao maior valor do conjunto.
"""

valor1 = int(input("Valor 1: "))
valor2 = int(input("Valor 2: "))
valor3 = int(input("Valor 3: "))

if valor1 >= valor2 and valor1 >= valor3:
    maior = valor1
elif valor2 >= valor1 and valor2 >= valor3:
    maior = valor2
else:
    maior = valor3

print(f"Maior valor: {maior}")
