# Eu to resumindo o elif assim:
# se o if não for verdadeiro, o programa tenta o elif.
# é tipo uma segunda chance para testar outra condição.

numero = int(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

print("Fim do programa.")

# Outro exemplo que parece coisa de aula.
# A nota decide se a pessoa foi aprovada ou não.
nota = float(input("Digite a nota do aluno (0-10): "))

if nota >= 9:
    print("Aprovado com louvor!")
elif nota >= 7:
    print("Aprovado!")
elif nota >= 5:
    print("Recuperação.")
else:
    print("Reprovado.")

print("Fim do programa.")

# Aqui eu testei o elif dentro de um for.
# É legal porque ele verifica cada número da lista por vez.
numeros = [10, -5, 0, 23, -1]
for numero in numeros:
    if numero > 0:
        print(f"{numero} é positivo.")
    elif numero < 0:
        print(f"{numero} é negativo.")
    else:
        print(f"{numero} é zero.")

print("Fim do programa.")