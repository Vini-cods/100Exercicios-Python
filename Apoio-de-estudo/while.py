# O while foi o primeiro loop que eu realmente entendi.
# Enquanto a condição for verdadeira, ele continua repetindo.
# Se não houver um jeito de parar, vira loop infinito e o programa trava.

# Sintaxe:
# while condicao:
#     bloco

# Exemplo 1: contagem simples
print("--- Exemplo 1: Contagem de 1 a 5 ---")
contador = 1
while contador <= 5:
    print(f"Contador está em: {contador}")
    contador += 1

print("Loop 1 finalizado.\n")

# Exemplo 2: jogo de adivinhar palavra
print("--- Exemplo 2: Adivinhe a palavra secreta ---")
palavra_secreta = "python"
palpite = ""

while palpite.lower() != palavra_secreta:
    palpite = input("Adivinhe a palavra secreta (ou digite 'sair'): ")
    if palpite.lower() == "sair":
        print("Que pena! Você desistiu.")
        break
    if palpite.lower() == palavra_secreta:
        print("Parabéns! Você acertou a palavra secreta!")
    else:
        print("Palpite incorreto. Tente novamente.")

print("Loop 2 finalizado.\n")

# Exemplo 3: usando continue para pular iteração
# A ideia aqui é só ignorar os números pares.
print("--- Exemplo 3: Imprimindo apenas números ímpares ---")
numero = 0
while numero < 10:
    numero += 1
    if numero % 2 == 0:
        continue
    print(f"Número ímpar: {numero}")

print("Loop 3 finalizado.\n")

# Exemplo 4: else no while
# Esse else executa quando o loop termina normalmente.
print("--- Exemplo 4: while com else ---")
tentativas = 3
while tentativas > 0:
    print(f"Você tem {tentativas} tentativas.")
    tentativas -= 1
else:
    print("O loop terminou porque as tentativas acabaram (sem 'break').")

print("Loop 4 finalizado.")