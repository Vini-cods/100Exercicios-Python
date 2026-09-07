"""
MÓDULO 02 - ESTRUTURAS CONDICIONAIS                          EXERCÍCIO 23

CALCULADORA COM TRATAMENTO DE ERROS

Enunciado:
    Leia dois números e um operador (+, -, *, /) e mostre o resultado
    da operação. Trate dois casos especiais: divisão por zero e
    operador não reconhecido.

Requisito:
    Utilize uma estrutura condicional para escolher a operação e
    trate os casos especiais antes de tentar calcular o resultado.

Exemplo de execução:
    Primeiro valor: 10
    Operador (+, -, *, /): /
    Segundo valor: 2
    Resultado: 5,00

Teste seu programa:
    Valor 1  Operador  Valor 2  ->  Resultado esperado
    10       +         2        ->  Resultado: 12,00
    10       /         0        ->  Erro: divisão por zero.
    10       ?         2        ->  Operador inválido.

Verificação final:
    Teste a divisão por zero separadamente de um operador inválido, e
    confirme que o programa nunca tenta realizar o cálculo nesses
    dois casos.
"""

valor1 = float(input("Primeiro valor: ").replace(",", "."))
operador = input("Operador (+, -, *, /): ")
valor2 = float(input("Segundo valor: ").replace(",", "."))

if operador == "+":
    resultado = valor1 + valor2
    print(f"Resultado: {resultado:.2f}".replace(".", ","))
elif operador == "-":
    resultado = valor1 - valor2
    print(f"Resultado: {resultado:.2f}".replace(".", ","))
elif operador == "*":
    resultado = valor1 * valor2
    print(f"Resultado: {resultado:.2f}".replace(".", ","))
elif operador == "/":
    if valor2 == 0:
        print("Erro: divisão por zero.")
    else:
        resultado = valor1 / valor2
        print(f"Resultado: {resultado:.2f}".replace(".", ","))
else:
    print("Operador inválido.")
