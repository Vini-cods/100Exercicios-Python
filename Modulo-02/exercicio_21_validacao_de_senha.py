"""
MÓDULO 02 - ESTRUTURAS CONDICIONAIS                          EXERCÍCIO 21

VALIDAÇÃO DE SENHA SIMPLES

Enunciado:
    Leia uma senha digitada pelo usuário e verifique se ela é
    considerada forte, segundo as regras abaixo.

Regra:
    Uma senha é forte quando, ao mesmo tempo:
      - tem pelo menos 8 caracteres;
      - contém pelo menos uma letra maiúscula;
      - contém pelo menos uma letra minúscula.
    Se qualquer uma dessas condições falhar, a senha é fraca.

Exemplo de execução:
    Digite uma senha: Python10
    Senha forte.

Teste seu programa:
    Entrada     ->  Resultado esperado
    Python10    ->  Senha forte.
    python10    ->  Senha fraca.
    ABC12345    ->  Senha fraca.
    curta1A     ->  Senha fraca.

Verificação final:
    Teste uma senha com exatamente 8 caracteres que tenha letra
    maiúscula e minúscula ao mesmo tempo (ex.: "SenhaBoa") e confirme
    que ela é aceita como forte.
"""

senha = input("Digite uma senha: ")

tem_tamanho = len(senha) >= 8
tem_maiuscula = senha != senha.lower()
tem_minuscula = senha != senha.upper()

if tem_tamanho and tem_maiuscula and tem_minuscula:
    print("Senha forte.")
else:
    print("Senha fraca.")
