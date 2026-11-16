# Esse exercício me ajudou a fixar a lógica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

# Esse exercÃ­cio me ajudou a fixar a lÃ³gica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

# ExercÃ­cio 08 - Desconto no produto
#
# Regra: Desconto = preÃ§o Ã— 10%
# ":.2f" formata o nÃºmero com duas casas decimais (padrÃ£o de dinheiro)

preco = float(input("PreÃ§o: "))

desconto = preco * 0.10
preco_final = preco - desconto

print(f"Desconto: R$ {desconto:.2f}")
print(f"PreÃ§o final: R$ {preco_final:.2f}")

