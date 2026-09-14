"""
Módulo 02 - Estruturas Condicionais
Exercício 27 - Classificação de IMC

Enunciado:
Leia o peso em quilogramas e a altura em metros. Calcule o IMC e
classifique o resultado usando apenas as regras didáticas da tabela.

Regra:
IMC = peso / (altura x altura)

Regras do exercício:
Menor que 18,5                       -> ABAIXO DA FAIXA
Maior ou igual a 18,5 e menor que 25 -> FAIXA NORMAL
Maior ou igual a 25 e menor que 30   -> ACIMA DA FAIXA
Maior ou igual a 30                  -> FAIXA ELEVADA

Observação: classificação didática usada apenas para praticar lógica
de programação, não é orientação médica.
"""


def ler_float(mensagem):
    texto = input(mensagem).strip().replace(",", ".")
    return float(texto)


def formatar(valor, casas=1):
    return f"{valor:.{casas}f}".replace(".", ",")


peso = ler_float("Peso (kg): ")
altura = ler_float("Altura (m): ")

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "ABAIXO DA FAIXA"
elif imc < 25:
    classificacao = "FAIXA NORMAL"
elif imc < 30:
    classificacao = "ACIMA DA FAIXA"
else:
    classificacao = "FAIXA ELEVADA"

print(f"\nIMC: {formatar(imc)}")
print(f"Classificação: {classificacao}")

# Teste seu programa (valores da apostila):
# 50 kg, 1,70 m -> ABAIXO DA FAIXA
# 80 kg, 1,80 m -> FAIXA NORMAL
# 90 kg, 1,70 m -> FAIXA ELEVADA
