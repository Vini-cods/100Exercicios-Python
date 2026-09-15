# Esse exercício me ajudou a fixar a lógica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

# Esse exercÃ­cio me ajudou a fixar a lÃ³gica do problema.
# Eu li os dados, apliquei a regra e mostrei o resultado.

"""
MÃ³dulo 02 - Estruturas Condicionais
ExercÃ­cio 18 - Maior de dois nÃºmeros

Enunciado:
Leia dois nÃºmeros reais e mostre qual deles Ã© o maior. Se os valores
forem iguais, informe que nÃ£o existe maior.
"""


def ler_float(mensagem):
    """LÃª um nÃºmero real aceitando vÃ­rgula ou ponto como separador decimal."""
    texto = input(mensagem).strip().replace(",", ".")
    return float(texto)


def fmt_num(valor):
    """Mostra nÃºmeros inteiros sem casas decimais desnecessÃ¡rias."""
    if valor == int(valor):
        return str(int(valor))
    return str(valor).replace(".", ",")


primeiro = ler_float("Primeiro valor: ")
segundo = ler_float("Segundo valor: ")

if primeiro > segundo:
    print(f"\nMaior valor: {fmt_num(primeiro)}")
elif segundo > primeiro:
    print(f"\nMaior valor: {fmt_num(segundo)}")
else:
    print("\nResultado: VALORES IGUAIS (nÃ£o existe maior valor)")

# Teste seu programa (valores da apostila):
# 4, 9   -> 9
# -2, -8 -> -2
# 5, 5   -> VALORES IGUAIS

