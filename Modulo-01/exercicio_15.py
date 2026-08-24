# Exercício 15 - Custo final da compra
#
# Regra: subtotal = preço unitário × quantidade
#        total = subtotal + frete

preco_unitario = float(input("Preço unitário: "))
quantidade = float(input("Quantidade: "))
frete = float(input("Frete: "))

subtotal = preco_unitario * quantidade
total = subtotal + frete

print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Total: R$ {total:.2f}")
