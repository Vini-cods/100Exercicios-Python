"""
MÓDULO 02 - ESTRUTURAS CONDICIONAIS                          EXERCÍCIO 20

DIA DA SEMANA

Enunciado:
    Leia um número inteiro de 1 a 7 e mostre o nome do dia da semana
    correspondente, sabendo que 1 representa Domingo e 7 representa
    Sábado. Caso o número esteja fora desse intervalo, informe que o
    valor é inválido.

Regra:
    1 -> Domingo         2 -> Segunda-feira    3 -> Terça-feira
    4 -> Quarta-feira    5 -> Quinta-feira     6 -> Sexta-feira
    7 -> Sábado

Exemplo de execução:
    Número do dia (1 a 7): 4
    Dia da semana: Quarta-feira

Teste seu programa:
    Entrada  ->  Resultado esperado
    1        ->  Dia da semana: Domingo
    7        ->  Dia da semana: Sábado
    0        ->  Número inválido.
    9        ->  Número inválido.

Verificação final:
    Teste os valores 0 e 8, que ficam logo fora dos dois limites do
    intervalo válido (1 e 7).
"""

numero = int(input("Número do dia (1 a 7): "))

if numero == 1:
    print("Dia da semana: Domingo")
elif numero == 2:
    print("Dia da semana: Segunda-feira")
elif numero == 3:
    print("Dia da semana: Terça-feira")
elif numero == 4:
    print("Dia da semana: Quarta-feira")
elif numero == 5:
    print("Dia da semana: Quinta-feira")
elif numero == 6:
    print("Dia da semana: Sexta-feira")
elif numero == 7:
    print("Dia da semana: Sábado")
else:
    print("Número inválido.")
