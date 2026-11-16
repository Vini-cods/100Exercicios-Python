# O or é o contrário do and em um certo sentido.
# Ele retorna True se pelo menos uma condição for verdadeira.
# Quando eu vejo isso, penso: 'se alguma coisa bater, pode seguir'.

# Exemplo 1: uma condição é verdadeira
tem_dinheiro = True
tem_credito = False

if tem_dinheiro or tem_credito:
    print("Você pode comprar o item.")
else:
    print("Você não tem fundos suficientes.")

# Exemplo 2: as duas condições são verdadeiras
tem_sol = True
fim_de_semana = True

if tem_sol or fim_de_semana:
    print("Vamos à praia!")
else:
    print("Vamos ficar em casa.")

# Exemplo 3: as duas são falsas
esta_chovendo = False
esta_frio = False

if esta_chovendo or esta_frio:
    print("Leve um casaco ou um guarda-chuva.")
else:
    print("O tempo está agradável.")

# Exemplo com entrada do usuário
try:
    idade_str = input("Digite sua idade: ")
    idade = int(idade_str)

    # Aqui a ideia é: criança ou idosa ganha desconto.
    if idade < 12 or idade > 65:
        print("Você tem direito a um desconto.")
    else:
        print("Você não tem direito a um desconto.")
except ValueError:
    print("Por favor, digite um número válido para a idade.")