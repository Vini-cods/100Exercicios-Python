# Esse exercício me ajudou a fixar a lógica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

# Esse exercÃ­cio me ajudou a fixar a lÃ³gica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

"""
MÃ³dulo 02 - Estruturas Condicionais
ExercÃ­cio 30 - AprovaÃ§Ã£o de emprÃ©stimo

Enunciado:
Leia o valor de um imÃ³vel, o salÃ¡rio mensal do comprador e o prazo de
pagamento em anos. Calcule a prestaÃ§Ã£o mensal e informe se o
emprÃ©stimo foi aprovado.

Regra:
PrestaÃ§Ã£o = valor do imÃ³vel / (anos x 12)
O emprÃ©stimo Ã© aprovado quando a prestaÃ§Ã£o nÃ£o ultrapassa 30% do
salÃ¡rio.

Requisito:
Mostre o valor da prestaÃ§Ã£o e o limite de 30% do salÃ¡rio.
"""


def ler_float(mensagem):
    texto = input(mensagem).strip().replace(",", ".")
    return float(texto)


def formatar_moeda(valor):
    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {texto}"


valor_imovel = ler_float("Valor do imÃ³vel: R$ ")
salario = ler_float("SalÃ¡rio: R$ ")
anos = int(input("Prazo (anos): "))

prestacao = valor_imovel / (anos * 12)
limite = salario * 0.30

if prestacao <= limite:
    resultado = "APROVADO"
else:
    resultado = "NEGADO"

print(f"\nPrestaÃ§Ã£o: {formatar_moeda(prestacao)}")
print(f"Limite: {formatar_moeda(limite)}")
print(f"Resultado: {resultado}")

# Teste seu programa (valores da apostila):
# R$ 120.000, salÃ¡rio R$ 2.000, 20 anos -> APROVADO
# R$ 300.000, salÃ¡rio R$ 3.000, 15 anos -> NEGADO
# R$ 216.000, salÃ¡rio R$ 2.000, 30 anos -> APROVADO

