"""
MÓDULO 02 - ESTRUTURAS CONDICIONAIS                          EXERCÍCIO 18

ÍNDICE DE MASSA CORPORAL (IMC)

Enunciado:
    Leia o peso (em kg) e a altura (em metros) de uma pessoa. Calcule
    o IMC e mostre a classificação correspondente.

Regra:
    IMC = peso ÷ (altura × altura).
    IMC < 18,5          -> Abaixo do peso
    18,5 <= IMC < 25,0   -> Peso normal
    25,0 <= IMC < 30,0   -> Sobrepeso
    IMC >= 30,0          -> Obesidade

Exemplo de execução:
    Peso (kg): 70
    Altura (m): 1,75
    IMC: 22,86
    Classificação: Peso normal

Teste seu programa:
    Peso   Altura  ->  Classificação esperada
    50     1,70    ->  Abaixo do peso
    68     1,70    ->  Peso normal
    80     1,70    ->  Sobrepeso
    95     1,70    ->  Obesidade

Verificação final:
    Ajuste peso e altura até obter um IMC exatamente igual a 25,0 e
    confirme que esse caso cai em "Sobrepeso", não em "Peso normal".
"""

peso = float(input("Peso (kg): ").replace(",", "."))
altura = float(input("Altura (m): ").replace(",", "."))
imc = peso / (altura ** 2)
imc_str = f"{imc:.2f}".replace(".", ",")

print(f"IMC: {imc_str}")

if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25.0:
    print("Classificação: Peso normal")
elif imc < 30.0:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obesidade")
