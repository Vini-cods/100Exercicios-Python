"""
MÓDULO 02 - ESTRUTURAS CONDICIONAIS                          EXERCÍCIO 19

DESCONTO POR FAIXA DE VALOR

Enunciado:
    Leia o valor total de uma compra e aplique um desconto de acordo
    com a faixa de valor. Mostre o valor do desconto e o valor final
    a pagar.

Regra:
    Até R$ 100,00                -> sem desconto
    De R$ 100,01 até R$ 300,00   -> 5% de desconto
    De R$ 300,01 até R$ 800,00   -> 10% de desconto
    Acima de R$ 800,00           -> 15% de desconto

Exemplo de execução:
    Valor da compra: R$ 500,00
    Desconto: R$ 50,00
    Valor final: R$ 450,00

Teste seu programa:
    Valor       ->  Desconto esperado  ->  Valor final esperado
    80,00       ->  0,00               ->  80,00
    100,00      ->  0,00               ->  100,00
    300,00      ->  15,00              ->  285,00
    1000,00     ->  150,00             ->  850,00

Verificação final:
    Teste exatamente os valores R$ 100,00, R$ 300,00 e R$ 800,00; eles
    marcam a virada entre uma faixa e a próxima.
"""

valor = float(input("Valor da compra: R$ ").replace(",", "."))

if valor <= 100:
    percentual = 0
elif valor <= 300:
    percentual = 0.05
elif valor <= 800:
    percentual = 0.10
else:
    percentual = 0.15

desconto = valor * percentual
valor_final = valor - desconto

desconto_str = f"{desconto:.2f}".replace(".", ",")
valor_final_str = f"{valor_final:.2f}".replace(".", ",")

print(f"Desconto: R$ {desconto_str}")
print(f"Valor final: R$ {valor_final_str}")
