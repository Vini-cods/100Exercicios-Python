"""
MÓDULO 02 - ESTRUTURAS CONDICIONAIS                          EXERCÍCIO 13

SITUAÇÃO DE APROVAÇÃO

Enunciado:
    Leia duas notas de um aluno, calcule a média aritmética e informe
    a situação final: Aprovado, Recuperação ou Reprovado.

Regra:
    Média = (nota 1 + nota 2) ÷ 2.
    Média >= 6,0            -> Aprovado
    4,0 <= Média < 6,0      -> Recuperação
    Média < 4,0             -> Reprovado

Exemplo de execução:
    Nota 1: 7
    Nota 2: 5
    Média: 6,0
    Situação: Aprovado

Teste seu programa:
    Nota 1  Nota 2  ->  Média  ->  Situação esperada
    8       9       ->  8,5    ->  Aprovado
    5       3       ->  4,0    ->  Recuperação
    2       3       ->  2,5    ->  Reprovado

Verificação final:
    Teste uma média exatamente igual a 6,0 e outra exatamente igual a
    4,0; ambas ficam no limite entre duas situações diferentes.
"""

nota1 = float(input("Nota 1: ").replace(",", "."))
nota2 = float(input("Nota 2: ").replace(",", "."))
media = (nota1 + nota2) / 2
media_str = f"{media:.1f}".replace(".", ",")

print(f"Média: {media_str}")

if media >= 6.0:
    print("Situação: Aprovado")
elif media >= 4.0:
    print("Situação: Recuperação")
else:
    print("Situação: Reprovado")
