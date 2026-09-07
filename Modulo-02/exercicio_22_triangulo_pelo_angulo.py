"""
MÓDULO 02 - ESTRUTURAS CONDICIONAIS                          EXERCÍCIO 22

TRIÂNGULO: CLASSIFICAÇÃO PELO ÂNGULO

Enunciado:
    Leia três lados que já formam um triângulo válido e classifique-o
    quanto ao ângulo em Retângulo, Acutângulo ou Obtusângulo.

Regra:
    Considere C o maior dos três lados, e A e B os outros dois.
    A² + B² = C²   -> Retângulo
    A² + B² > C²   -> Acutângulo
    A² + B² < C²   -> Obtusângulo

Exemplo de execução:
    Lado A: 3
    Lado B: 4
    Lado C: 5
    Classificação: Retângulo

Teste seu programa:
    A     B     C     ->  Resultado esperado
    3     4     5     ->  Retângulo
    4     4     4     ->  Acutângulo
    4     5     7     ->  Obtusângulo

Verificação final:
    Repita o teste trocando a ordem dos lados na digitação (ex.: 5, 3
    e 4 em vez de 3, 4 e 5) e confirme que o resultado não muda, já
    que o programa deve identificar sozinho qual é o maior lado.
"""

a = float(input("Lado A: ").replace(",", "."))
b = float(input("Lado B: ").replace(",", "."))
c = float(input("Lado C: ").replace(",", "."))

if a >= b and a >= c:
    maior, lado1, lado2 = a, b, c
elif b >= a and b >= c:
    maior, lado1, lado2 = b, a, c
else:
    maior, lado1, lado2 = c, a, b

soma_quadrados = lado1 ** 2 + lado2 ** 2
quadrado_maior = maior ** 2

if soma_quadrados == quadrado_maior:
    print("Classificação: Retângulo")
elif soma_quadrados > quadrado_maior:
    print("Classificação: Acutângulo")
else:
    print("Classificação: Obtusângulo")
