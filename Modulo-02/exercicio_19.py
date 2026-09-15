# Esse exercício me ajudou a fixar a lógica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

# Esse exercÃ­cio me ajudou a fixar a lÃ³gica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

"""
MÃ³dulo 02 - Estruturas Condicionais
ExercÃ­cio 19 - Maior e menor de trÃªs nÃºmeros

Enunciado:
Leia trÃªs nÃºmeros reais e mostre o maior e o menor valor informado.

Requisito:
O programa deve funcionar tambÃ©m quando houver valores repetidos.
"""

entrada = input("Valores (separados por vÃ­rgula): ")
valores = [float(v.strip().replace(",", ".")) for v in entrada.split(",")]

maior = max(valores)
menor = min(valores)


def fmt_num(valor):
    if valor == int(valor):
        return str(int(valor))
    return str(valor).replace(".", ",")


print(f"\nMaior: {fmt_num(maior)}")
print(f"Menor: {fmt_num(menor)}")

# Teste seu programa (valores da apostila):
# 3, 9, 5    -> Maior: 9  | Menor: 3
# -4, -1, -7 -> Maior: -1 | Menor: -7
# 6, 6, 2    -> Maior: 6  | Menor: 2

