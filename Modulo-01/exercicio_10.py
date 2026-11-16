# Esse exercício me ajudou a fixar a lógica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

# Esse exercÃ­cio me ajudou a fixar a lÃ³gica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

# ExercÃ­cio 10 - SalÃ¡rio com comissÃ£o
#
# Regra: comissÃ£o = vendas Ã— 4%
#        salÃ¡rio total = salÃ¡rio fixo + comissÃ£o

salario_fixo = float(input("SalÃ¡rio fixo: "))
total_vendido = float(input("Total vendido: "))

comissao = total_vendido * 0.04
salario_total = salario_fixo + comissao

print(f"ComissÃ£o: R$ {comissao:.2f}")
print(f"SalÃ¡rio total: R$ {salario_total:.2f}")

