# Aqui eu to anotando o básico do if.
# Se a condição for verdadeira, entra no bloco.
# Se for falsa, ele simplesmente ignora e segue em frente.

print("--- Exemplo 1: if simples ---")
idade = 20
print(f"Idade informada: {idade}")

if idade >= 18:
    print("Acesso permitido. Você é maior de idade.")

# Eu também acho útil pensar no else como o 'caso contrário'.
# Quando o if não dá certo, o else entra em ação.

print("--- Exemplo 2: if com else ---")
idade = 16
print(f"Idade informada: {idade}")

if idade >= 18:
    print("Acesso permitido. Você é maior de idade.")
else:
    print("Acesso negado. Você é menor de idade.")

# O elif parece um 'if extra' para testar outra condição.
# Ele é bom quando tem mais de dois caminhos possíveis.

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

# Isso aqui é tipo misturar condições com and, or e not.
# Dá pra fazer decisões mais "inteligentes" sem explodir a cabeça.

print("--- Exemplo 4: condicionais com operadores lógicos ---")
temperatura = 15
chovendo = False
print(f"Condições atuais -> Temperatura: {temperatura}°C, Chovendo: {chovendo}")

if temperatura > 20 and not chovendo:
    print("Está um dia agradável para passear.")
elif temperatura <= 15 or chovendo:
    print("Talvez seja melhor ficar em casa hoje.")
else:
    print("O tempo está bom!")