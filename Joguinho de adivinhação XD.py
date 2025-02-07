import random

print("Bem-vindo ao Jogo de Adivinhação!")
numero_secreto = random.randint(1,10)
tentativas = 0

while True:
    tentativa = int(input("Adivinhe um número entre 1 e 10: "))
    tentativas += 1

    if tentativa < numero_secreto:
        print("O número é maior! Tente novamente.")
    elif tentativa > numero_secreto:
        print("O número é menor! Tente novamente.")
    else:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break
