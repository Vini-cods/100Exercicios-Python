# Exercício 08 - Desconto no produto
#
# Regra: Desconto = preço × 10%
# ":.2f" formata o número com duas casas decimais (padrão de dinheiro)

preco = float(input("Preço: "))

desconto = preco * 0.10
preco_final = preco - desconto

print(f"Desconto: R$ {desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")
