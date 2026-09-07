"""
MÓDULO 02 - ESTRUTURAS CONDICIONAIS                          EXERCÍCIO 16

TRIÂNGULO: EXISTÊNCIA E TIPO PELOS LADOS

Enunciado:
    Leia três medidas de lados. Primeiro verifique se elas formam um
    triângulo válido; se formarem, classifique-o em Equilátero,
    Isósceles ou Escaleno.

Regra:
    Três lados formam um triângulo válido quando a soma de quaisquer
    dois lados é maior que o terceiro lado.
    Equilátero  -> os três lados são iguais.
    Isósceles   -> exatamente dois lados são iguais.
    Escaleno    -> os três lados são diferentes.

Exemplo de execução:
    Lado A: 5
    Lado B: 5
    Lado C: 8
    Classificação: Isósceles

Teste seu programa:
    A     B     C     ->  Resultado esperado
    4     4     4     ->  Equilátero
    5     5     8     ->  Isósceles
    3     4     5     ->  Escaleno
    1     1     5     ->  Não forma um triângulo.

Verificação final:
    Teste um conjunto de lados que não forma triângulo (como 1, 1 e
    5) e confirme que o programa não tenta classificá-lo por tipo.
"""

a = float(input("Lado A: ").replace(",", "."))
b = float(input("Lado B: ").replace(",", "."))
c = float(input("Lado C: ").replace(",", "."))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Classificação: Equilátero")
    elif a == b or a == c or b == c:
        print("Classificação: Isósceles")
    else:
        print("Classificação: Escaleno")
else:
    print("Não forma um triângulo.")
