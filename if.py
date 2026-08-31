# Este arquivo demonstra o uso de estruturas condicionais (if, elif, else) em Python.

print("--- Exemplo 1: Simples if ---")
idade = 20
print(f"Idade informada: {idade}")

if idade >= 18:
    print("Acesso permitido. Você é maior de idade.")


# o if serve para verificar uma condição e executar um bloco de código se a condição for verdadeira.

# O comando `else` pode ser usado com o `if` para fornecer um bloco de código alternativo
# que será executado se a condição do `if` for falsa.

print("--- Exemplo 2: if-else ---")
idade = 16
print(f"Idade informada: {idade}")

if idade >= 18:
    print("Acesso permitido. Você é maior de idade.")
else:
    print("Acesso negado. Você é menor de idade.")

# O comando `elif` (abreviação de "else if") permite verificar múltiplas condições.

print("--- Exemplo 3: if-elif-else ---")
nota = 85
print(f"Nota informada: {nota}")

if nota >= 90:
    print("Parabéns! Você obteve um excelente desempenho.")
elif nota >= 80:
    print("Você obteve um bom desempenho.")
elif nota >= 70:
    print("Você obteve um desempenho satisfatório.")
elif nota >= 60:
    print("Você obteve um desempenho regular.")
elif nota >= 50:
    print("Você obteve um desempenho abaixo da média.")
else:
   print("Você precisa melhorar.") 

#O elif permite verificar várias condições em sequência, e o bloco de código correspondente à primeira condição verdadeira será executado. Se nenhuma das condições for verdadeira, o bloco de código do `else` será executado.

