# Esse exercício me ajudou a fixar a lógica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

# Esse exercÃ­cio me ajudou a fixar a lÃ³gica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

# ExercÃ­cio 15 - Custo final da compra
#
# Regra: subtotal = preÃ§o unitÃ¡rio Ã— quantidade
#        total = subtotal + frete

preco_unitario = float(input("PreÃ§o unitÃ¡rio: "))
quantidade = float(input("Quantidade: "))
frete = float(input("Frete: "))

subtotal = preco_unitario * quantidade
total = subtotal + frete

print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Total: R$ {total:.2f}")

