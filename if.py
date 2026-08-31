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