# Eu achei o range bem útil porque ele gera números sem eu precisar escrever tudo manualmente.
# É tipo um atalho para fazer loop de números.

# Sintaxe:
# range(stop)
# range(start, stop)
# range(start, stop, step)

# Exemplo 1: só com stop
# Gera 0 até 4
print("--- range(5) ---")
for numero in range(5):
    print(f"Número: {numero}")

# Exemplo 2: com start e stop
# Gera 2 até 6
print("\n--- range(2, 7) ---")
for numero in range(2, 7):
    print(f"Número: {numero}")

# Exemplo 3: com step
# Gera números pares de 0 a 10
print("\n--- range(0, 11, 2) ---")
for numero in range(0, 11, 2):
    print(f"Número par: {numero}")

# Exemplo 4: contagem regressiva
# Quando o step é negativo, a ordem é invertida.
print("\n--- range(5, 0, -1) ---")
for numero in range(5, 0, -1):
    print(f"Contagem regressiva: {numero}")
print("Fogo!")

# O range não é uma lista, ele é um objeto especial do tipo range.
meu_range = range(10)
print(f"\nO tipo do objeto criado é: {type(meu_range)}")
print(f"O objeto em si: {meu_range}")

# Se eu quiser ver todos os números na tela, posso transformar em lista.
lista_de_numeros = list(meu_range)
print(f"O objeto range convertido para lista: {lista_de_numeros}")