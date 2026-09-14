"""
Módulo 02 - Estruturas Condicionais
Exercício 35 - Valor do ingresso

Enunciado:
O ingresso custa R$ 30,00. Leia a idade e informe se a pessoa é
estudante. Calcule o valor final conforme as regras.

Regra:
Paga meia-entrada quem tiver menos de 12 anos, quem for estudante ou
quem tiver 60 anos ou mais. O desconto é de 50% e não é acumulativo.
"""


def formatar_moeda(valor):
    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {texto}"


PRECO_CHEIO = 30.00

idade = int(input("Idade: "))
estudante = input("Estudante (SIM/NÃO): ").strip().upper()

if idade < 12 or estudante == "SIM" or idade >= 60:
    valor_final = PRECO_CHEIO * 0.5
else:
    valor_final = PRECO_CHEIO

print(f"\nValor do ingresso: {formatar_moeda(valor_final)}")

# Teste seu programa (valores da apostila):
# Idade 10, Estudante NÃO -> R$ 15,00
# Idade 25, Estudante SIM -> R$ 15,00
# Idade 65, Estudante NÃO -> R$ 15,00
# Idade 30, Estudante NÃO -> R$ 30,00
