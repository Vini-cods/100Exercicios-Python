"""
Módulo 02 - Estruturas Condicionais
Exercício 30 - Aprovação de empréstimo

Enunciado:
Leia o valor de um imóvel, o salário mensal do comprador e o prazo de
pagamento em anos. Calcule a prestação mensal e informe se o
empréstimo foi aprovado.

Regra:
Prestação = valor do imóvel / (anos x 12)
O empréstimo é aprovado quando a prestação não ultrapassa 30% do
salário.

Requisito:
Mostre o valor da prestação e o limite de 30% do salário.
"""


def ler_float(mensagem):
    texto = input(mensagem).strip().replace(",", ".")
    return float(texto)


def formatar_moeda(valor):
    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {texto}"


valor_imovel = ler_float("Valor do imóvel: R$ ")
salario = ler_float("Salário: R$ ")
anos = int(input("Prazo (anos): "))

prestacao = valor_imovel / (anos * 12)
limite = salario * 0.30

if prestacao <= limite:
    resultado = "APROVADO"
else:
    resultado = "NEGADO"

print(f"\nPrestação: {formatar_moeda(prestacao)}")
print(f"Limite: {formatar_moeda(limite)}")
print(f"Resultado: {resultado}")

# Teste seu programa (valores da apostila):
# R$ 120.000, salário R$ 2.000, 20 anos -> APROVADO
# R$ 300.000, salário R$ 3.000, 15 anos -> NEGADO
# R$ 216.000, salário R$ 2.000, 30 anos -> APROVADO
