# Esse exercício me ajudou a fixar a lógica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

# Esse exercÃ­cio me ajudou a fixar a lÃ³gica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

"""
MÃ³dulo 02 - Estruturas Condicionais
ExercÃ­cio 25 - PreÃ§o conforme a forma de pagamento

Enunciado:
Leia o preÃ§o de um produto e a opÃ§Ã£o de pagamento. Calcule e mostre
o valor final conforme a tabela.

Regras do exercÃ­cio:
1 - Dinheiro ou Pix     -> 10% de desconto
2 - DÃ©bito              -> 5% de desconto
3 - CrÃ©dito Ã  vista     -> sem alteraÃ§Ã£o
4 - CrÃ©dito parcelado   -> 8% de acrÃ©scimo
"""


def ler_float(mensagem):
    texto = input(mensagem).strip().replace(",", ".")
    return float(texto)


def formatar_moeda(valor):
    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {texto}"


preco = ler_float("PreÃ§o: R$ ")
opcao = int(input("OpÃ§Ã£o: "))

fatores = {1: 0.90, 2: 0.95, 3: 1.00, 4: 1.08}

if opcao in fatores:
    valor_final = preco * fatores[opcao]
    print(f"\nValor final: {formatar_moeda(valor_final)}")
else:
    print("\nOpÃ§Ã£o invÃ¡lida.")

# Teste seu programa (valores da apostila):
# R$ 100,00, opÃ§Ã£o 2 -> R$ 95,00
# R$ 100,00, opÃ§Ã£o 3 -> R$ 100,00
# R$ 100,00, opÃ§Ã£o 4 -> R$ 108,00

