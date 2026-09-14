"""
Módulo 02 - Estruturas Condicionais
Exercício 25 - Preço conforme a forma de pagamento

Enunciado:
Leia o preço de um produto e a opção de pagamento. Calcule e mostre
o valor final conforme a tabela.

Regras do exercício:
1 - Dinheiro ou Pix     -> 10% de desconto
2 - Débito              -> 5% de desconto
3 - Crédito à vista     -> sem alteração
4 - Crédito parcelado   -> 8% de acréscimo
"""


def ler_float(mensagem):
    texto = input(mensagem).strip().replace(",", ".")
    return float(texto)


def formatar_moeda(valor):
    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {texto}"


preco = ler_float("Preço: R$ ")
opcao = int(input("Opção: "))

fatores = {1: 0.90, 2: 0.95, 3: 1.00, 4: 1.08}

if opcao in fatores:
    valor_final = preco * fatores[opcao]
    print(f"\nValor final: {formatar_moeda(valor_final)}")
else:
    print("\nOpção inválida.")

# Teste seu programa (valores da apostila):
# R$ 100,00, opção 2 -> R$ 95,00
# R$ 100,00, opção 3 -> R$ 100,00
# R$ 100,00, opção 4 -> R$ 108,00
