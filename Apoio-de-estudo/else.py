# Esse aqui eu usei para entender o else de verdade.
# O else entra quando o if não é atendido.
# Tipo: 'se isso não deu, faz isso aqui'.

a = 10
b = 20

if a > b:
    print("a é maior que b")
else:
    print("a não é maior que b")

# Também vi que o else funciona em loop for.
# Quando o loop termina normalmente, ele pode executar esse bloco.
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)
else:
    print("Fim da lista de números.")

# No while também funciona assim.
# Então o else é um jeito de dizer: 'loop terminou sem dar problema'.
contador = 1
while contador <= 5:
    print(contador)
    contador += 1
else:
    print("Contagem concluída.")