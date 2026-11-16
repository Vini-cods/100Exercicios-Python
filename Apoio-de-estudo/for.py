# O for é o meu jeito de dizer: 'vai percorrer cada item desta lista'.
# Parece meio óbvio, mas quando pega o jeito, ele facilita muito.

print("--- Iterando sobre uma lista de frutas ---")
frutas = ["maçã", "banana", "laranja", "morango"]
for fruta in frutas:
    print(f"A fruta da vez é: {fruta}")

# Aqui eu testei em string, que também é uma sequência.
print("\n--- Iterando sobre uma string ---")
palavra = "Python"
for letra in palavra:
    print(f"Letra: {letra}")

# O range é bem útil pra repetir coisas sem escrever manualmente.
print("\n--- Utilizando range(5) ---")
for numero in range(5):
    print(f"Número: {numero}")

print("\n--- Utilizando range(1, 6) ---")
for numero in range(1, 6):
    print(f"Número: {numero}")

# Também dá pra percorrer dicionário, que é tipo um mapa de chave e valor.
print("\n--- Iterando sobre um dicionário de contatos ---")
contatos = {
    "João": "joao@example.com",
    "Maria": "maria@example.com",
    "Pedro": "pedro@example.com"
}

print("\nNomes (chaves) no dicionário:")
for nome in contatos:
    print(nome)

print("\nE-mails (valores) no dicionário:")
for email in contatos.values():
    print(email)

print("\nContatos completos (chave e valor):")
for nome, email in contatos.items():
    print(f"O e-mail de {nome} é {email}")

# O enumerate me ajudou a entender que dá pra pegar a posição junto com o valor.
print("\n--- Usando enumerate para listar o ranking de filmes ---")
filmes_ranking = ["O Poderoso Chefão", "Um Sonho de Liberdade", "Batman: O Cavaleiro das Trevas"]
for i, filme in enumerate(filmes_ranking):
    print(f"#{i + 1}: {filme}")