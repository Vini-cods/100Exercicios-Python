"""
MÓDULO 02 - ESTRUTURAS CONDICIONAIS                          EXERCÍCIO 09

PAR OU ÍMPAR

Enunciado:
    Leia um número inteiro e informe se ele é par ou ímpar.

Regra:
    Um número é par quando o resto da divisão por 2 é igual a 0.

Exemplo de execução:
    Digite um número inteiro: 7
    7 é ímpar.

Teste seu programa:
    Entrada  ->  Resultado esperado
    4        ->  4 é par.
    7        ->  7 é ímpar.
    0        ->  0 é par.
    -3       ->  -3 é ímpar.

Verificação final:
    Teste com zero (deve ser tratado como par) e com um número
    negativo ímpar, garantindo que o sinal não interfere na regra.
"""

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print(f"{numero} é par.")
else:
    print(f"{numero} é ímpar.")
