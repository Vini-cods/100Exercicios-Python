# Exercício 09 - Reajuste salarial
#
# Regra: aumento = salário × 15%
#        novo salário = salário + aumento

salario = float(input("Salário atual: "))

aumento = salario * 0.15
novo_salario = salario + aumento

print(f"Aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")
