# O is me confundiu um pouco no começo.
# Ele não compara valor, ele compara se são o mesmo objeto na memória.
# Ou seja, se duas variáveis apontam para a mesma coisa.

# Exemplo com inteiros (imutáveis)
a = 5
b = 5
print(f"a = {a}, b = {b}")
print(f"a is b: {a is b}")

c = 257
d = 257
print(f"c = {c}, d = {d}")
print(f"c is d: {c is d}")

# Exemplo com listas (mutáveis)
list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a

print("\nListas:")
print(f"list_a = {list_a}")
print(f"list_b = {list_b}")
print(f"list_c = {list_c}")

# list_a e list_b têm o mesmo conteúdo, mas não são o mesmo objeto.
print(f"list_a is list_b: {list_a is list_b}")
print(f"list_a == list_b: {list_a == list_b}")

# list_a e list_c apontam para o mesmo objeto.
print(f"list_a is list_c: {list_a is list_c}")

# Se eu mexer em list_a, list_c também muda porque são a mesma lista.
list_a.append(4)
print(f"\nApós modificar list_a:")
print(f"list_a = {list_a}")
print(f"list_c = {list_c}")
print(f"list_a is list_c: {list_a is list_c}")