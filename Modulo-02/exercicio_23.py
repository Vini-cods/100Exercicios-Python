"""
Módulo 02 - Estruturas Condicionais
Exercício 23 - Categoria de votação

Enunciado:
Leia a idade de uma pessoa e informe a categoria de votação conforme
as regras didáticas da tabela.

Regras do exercício:
Menor de 16 anos    -> NÃO PODE VOTAR
16 ou 17 anos       -> VOTO OPCIONAL
De 18 a 69 anos     -> VOTO OBRIGATÓRIO
70 anos ou mais     -> VOTO OPCIONAL
"""

idade = int(input("Idade: "))

if idade < 16:
    categoria = "NÃO PODE VOTAR"
elif idade < 18:
    categoria = "VOTO OPCIONAL"
elif idade < 70:
    categoria = "VOTO OBRIGATÓRIO"
else:
    categoria = "VOTO OPCIONAL"

print(f"\nCategoria: {categoria}")

# Teste seu programa (valores da apostila):
# 15 -> NÃO PODE VOTAR
# 16 -> VOTO OPCIONAL
# 18 -> VOTO OBRIGATÓRIO
# 70 -> VOTO OPCIONAL
