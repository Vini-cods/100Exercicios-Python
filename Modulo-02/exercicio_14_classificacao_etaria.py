"""
MÓDULO 02 - ESTRUTURAS CONDICIONAIS                          EXERCÍCIO 14

CLASSIFICAÇÃO ETÁRIA

Enunciado:
    Leia a idade de uma pessoa, em anos completos, e classifique-a em
    uma das faixas abaixo.

Regra:
    0  a 12 anos    -> Criança
    13 a 17 anos    -> Adolescente
    18 a 59 anos    -> Adulto
    60 anos ou mais -> Idoso

Exemplo de execução:
    Idade: 15
    Classificação: Adolescente

Teste seu programa:
    Idade  ->  Classificação esperada
    8      ->  Criança
    17     ->  Adolescente
    59     ->  Adulto
    60     ->  Idoso

Verificação final:
    Teste as idades exatamente nos limites de cada faixa (12/13,
    17/18 e 59/60) e confirme que cada uma cai no grupo correto.
"""

idade = int(input("Idade: "))

if idade <= 12:
    print("Classificação: Criança")
elif idade <= 17:
    print("Classificação: Adolescente")
elif idade <= 59:
    print("Classificação: Adulto")
else:
    print("Classificação: Idoso")
