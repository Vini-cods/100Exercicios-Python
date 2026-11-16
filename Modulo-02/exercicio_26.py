# Esse exercício me ajudou a fixar a lógica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

# Esse exercÃ­cio me ajudou a fixar a lÃ³gica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

"""
MÃ³dulo 02 - Estruturas Condicionais
ExercÃ­cio 26 - Reajuste por faixa salarial

Enunciado:
Leia o salÃ¡rio atual e calcule o novo salÃ¡rio conforme a tabela de
reajuste.

Requisito:
Mostre o percentual aplicado, o valor do aumento e o novo salÃ¡rio.

Regras do exercÃ­cio:
AtÃ© R$ 1.500,00                     -> 15%
De R$ 1.500,01 atÃ© R$ 3.000,00      -> 10%
Acima de R$ 3.000,00                -> 5%
"""


def ler_float(mensagem):
    texto = input(mensagem).strip().replace(",", ".")
    return float(texto)


def formatar_moeda(valor):
    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {texto}"


salario = ler_float("SalÃ¡rio atual: R$ ")

if salario <= 1500:
    percentual = 0.15
elif salario <= 3000:
    percentual = 0.10
else:
    percentual = 0.05

aumento = salario * percentual
novo_salario = salario + aumento

print(f"\nPercentual aplicado: {int(percentual * 100)}%")
print(f"Valor do aumento: {formatar_moeda(aumento)}")
print(f"Novo salÃ¡rio: {formatar_moeda(novo_salario)}")

# Teste seu programa (valores da apostila):
# R$ 1.500,00 -> 15% -> Novo salÃ¡rio R$ 1.725,00
# R$ 3.000,00 -> 10% -> Novo salÃ¡rio R$ 3.300,00
# R$ 4.000,00 -> 5%  -> Novo salÃ¡rio R$ 4.200,00

