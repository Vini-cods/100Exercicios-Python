"""
MÓDULO 02 - ESTRUTURAS CONDICIONAIS                          EXERCÍCIO 15

ANO BISSEXTO

Enunciado:
    Leia um ano e informe se ele é bissexto.

Regra:
    Um ano é bissexto quando é divisível por 4 e (não é divisível por
    100 ou é divisível por 400).

Exemplo de execução:
    Ano: 2024
    2024 é bissexto.

Teste seu programa:
    Ano   ->  Resultado esperado
    2024  ->  2024 é bissexto.
    1900  ->  1900 não é bissexto.
    2000  ->  2000 é bissexto.
    2023  ->  2023 não é bissexto.

Verificação final:
    Os anos 1900 e 2000 são o caso-chave desta regra: os dois são
    divisíveis por 100, mas só 2000 também é divisível por 400.
"""

ano = int(input("Ano: "))

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print(f"{ano} é bissexto.")
else:
    print(f"{ano} não é bissexto.")
