"""
MÓDULO 02 - ESTRUTURAS CONDICIONAIS                          EXERCÍCIO 12

POSITIVO, NEGATIVO OU ZERO

Enunciado:
    Leia um número real e classifique-o como positivo, negativo ou
    zero.

Exemplo de execução:
    Digite um número: -4,5
    Classificação: Negativo

Teste seu programa:
    Entrada   ->  Resultado esperado
    10        ->  Classificação: Positivo
    0         ->  Classificação: Zero
    -0,001    ->  Classificação: Negativo

Verificação final:
    Confirme que o valor exatamente igual a zero cai no caso "Zero",
    e não é tratado como positivo nem como negativo.
"""

numero = float(input("Digite um número: ").replace(",", "."))

if numero > 0:
    print("Classificação: Positivo")
elif numero < 0:
    print("Classificação: Negativo")
else:
    print("Classificação: Zero")
