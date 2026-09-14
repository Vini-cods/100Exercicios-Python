"""
Módulo 02 - Estruturas Condicionais
Exercício 18 - Maior de dois números

Enunciado:
Leia dois números reais e mostre qual deles é o maior. Se os valores
forem iguais, informe que não existe maior.
"""


def ler_float(mensagem):
    """Lê um número real aceitando vírgula ou ponto como separador decimal."""
    texto = input(mensagem).strip().replace(",", ".")
    return float(texto)


def fmt_num(valor):
    """Mostra números inteiros sem casas decimais desnecessárias."""
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
    print("\nResultado: VALORES IGUAIS (não existe maior valor)")

# Teste seu programa (valores da apostila):
# 4, 9   -> 9
# -2, -8 -> -2
# 5, 5   -> VALORES IGUAIS
