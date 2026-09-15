# Esse exercício me ajudou a fixar a lógica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

# Esse exercÃ­cio me ajudou a fixar a lÃ³gica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

"""
MÃ³dulo 02 - Estruturas Condicionais
ExercÃ­cio 23 - Categoria de votaÃ§Ã£o

Enunciado:
Leia a idade de uma pessoa e informe a categoria de votaÃ§Ã£o conforme
as regras didÃ¡ticas da tabela.

Regras do exercÃ­cio:
Menor de 16 anos    -> NÃƒO PODE VOTAR
16 ou 17 anos       -> VOTO OPCIONAL
De 18 a 69 anos     -> VOTO OBRIGATÃ“RIO
70 anos ou mais     -> VOTO OPCIONAL
"""

idade = int(input("Idade: "))

if idade < 16:
    categoria = "NÃƒO PODE VOTAR"
elif idade < 18:
    categoria = "VOTO OPCIONAL"
elif idade < 70:
    categoria = "VOTO OBRIGATÃ“RIO"
else:
    categoria = "VOTO OPCIONAL"

print(f"\nCategoria: {categoria}")

# Teste seu programa (valores da apostila):
# 15 -> NÃƒO PODE VOTAR
# 16 -> VOTO OPCIONAL
# 18 -> VOTO OBRIGATÃ“RIO
# 70 -> VOTO OPCIONAL

