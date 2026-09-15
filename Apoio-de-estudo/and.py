# O and é tipo: 'só entra se todas as condições forem verdadeiras'.
# Se uma delas for falsa, o bloco do if nem entra.
# Isso é bem útil quando a gente quer exigir mais de uma condição ao mesmo tempo.

# Exemplo 1: as duas condições são verdadeiras
idade = 25
tem_carteira_de_motorista = True

if idade >= 18 and tem_carteira_de_motorista:
    print("Você pode dirigir.")
else:
    print("Você não pode dirigir.")

# Exemplo 2: uma condição falhou
idade = 17
tem_carteira_de_motorista = True

if idade >= 18 and tem_carteira_de_motorista:
    print("Você pode dirigir.")
else:
    print("Você não pode dirigir.")

# Exemplo 3: as duas falharam
idade = 16
tem_carteira_de_motorista = False

if idade >= 18 and tem_carteira_de_motorista:
    print("Você pode dirigir.")
else:
    print("Você não pode dirigir.")