import os

print("Acerte o número que eu estou pensando e ganhe um prêmio!")
print()
print("O prêmio cheio é de R$ 1.024.000")
print()
print("Para cada tentativa, o prêmio é divido por 2")
print()
print("Dica: É um número entre 1 e 30")
print()
input("ENTER para começar")

os.system("cls")

premio = 1024000
palpite = int(input("Digite seu palpite: "))
tentativas = 1

while palpite != 3:
    os.system("cls")
    premio /= 2
    tentativas += 1
    palpite = int(input(f"Errado, valendo agora R$ {premio}, digite seu novo palpite: "))

os.system("cls")
print(f"Parabéns, você acertou em {tentativas} tentativas!!!")
print()
print(f"Seu prêmio é de R$ {premio}")