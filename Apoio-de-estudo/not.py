# O not é o operador que inverte a lógica.
# Se a condição for True, ele vira False.
# Se for False, vira True.
# Na prática, ele é tipo a negação da ideia.

# Exemplo 1: invertendo um valor verdadeiro
tem_sol = True
if not tem_sol:
    print("Está chovendo.")
else:
    print("Está ensolarado.")

# Exemplo 2: invertendo um valor falso
chovendo = False
if not chovendo:
    print("Não está chovendo, vamos passear!")
else:
    print("Está chovendo, melhor ficar em casa.")

# Exemplo 3: usando not em outra condição
idade = 20
if not (idade < 18):
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")