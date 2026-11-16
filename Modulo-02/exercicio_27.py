# Esse exercício me ajudou a fixar a lógica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

# Esse exercÃ­cio me ajudou a fixar a lÃ³gica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

"""
MÃ³dulo 02 - Estruturas Condicionais
ExercÃ­cio 27 - ClassificaÃ§Ã£o de IMC

Enunciado:
Leia o peso em quilogramas e a altura em metros. Calcule o IMC e
classifique o resultado usando apenas as regras didÃ¡ticas da tabela.

Regra:
IMC = peso / (altura x altura)

Regras do exercÃ­cio:
Menor que 18,5                       -> ABAIXO DA FAIXA
Maior ou igual a 18,5 e menor que 25 -> FAIXA NORMAL
Maior ou igual a 25 e menor que 30   -> ACIMA DA FAIXA
Maior ou igual a 30                  -> FAIXA ELEVADA

ObservaÃ§Ã£o: classificaÃ§Ã£o didÃ¡tica usada apenas para praticar lÃ³gica
de programaÃ§Ã£o, nÃ£o Ã© orientaÃ§Ã£o mÃ©dica.
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
print(f"ClassificaÃ§Ã£o: {classificacao}")

# Teste seu programa (valores da apostila):
# 50 kg, 1,70 m -> ABAIXO DA FAIXA
# 80 kg, 1,80 m -> FAIXA NORMAL
# 90 kg, 1,70 m -> FAIXA ELEVADA

