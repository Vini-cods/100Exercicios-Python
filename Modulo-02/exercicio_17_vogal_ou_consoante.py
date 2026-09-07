"""
MÓDULO 02 - ESTRUTURAS CONDICIONAIS                          EXERCÍCIO 17

VOGAL OU CONSOANTE

Enunciado:
    Leia uma única letra e informe se ela é uma vogal ou uma
    consoante. O programa deve funcionar tanto com letras maiúsculas
    quanto minúsculas.

Exemplo de execução:
    Digite uma letra: E
    E é uma vogal.

Teste seu programa:
    Entrada  ->  Resultado esperado
    a        ->  a é uma vogal.
    B        ->  B é uma consoante.
    U        ->  U é uma vogal.
    z        ->  z é uma consoante.

Verificação final:
    Teste a mesma vogal em maiúscula e em minúscula (ex.: "A" e "a")
    e confirme que as duas são reconhecidas como vogal.
"""

letra = input("Digite uma letra: ")
letra_minuscula = letra.lower()

if letra_minuscula in ("a", "e", "i", "o", "u"):
    print(f"{letra} é uma vogal.")
else:
    print(f"{letra} é uma consoante.")
