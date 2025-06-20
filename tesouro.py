import os

mapa = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

tesouro = [2,1]

tentativas = 5

def exibirMapa():
    """Exibe o mapa do tesouro já formatado"""
    for linha in mapa:
        print(" | ".join(linha))
        print("-" * 10)

os.system("cls")

print("Este é o mapa do tesouro.")

exibirMapa()

print()
print("Você tem 5 tentativas para encontrar o tesouro, boa sorte!")
print()
print("INSTRUÇÕES:")
print()
print("Encontre o 💎 no mapa 3x3")
print()
input("ENTER para começar.")

os.system("cls")

def jogada():
    """Capturar a linha e a coluna do palpite"""

    palpite = []

    linha = input("Linha do palpite: (0, 1 ou 2) ")
    print()

    while linha not in ["0", "1", "2"]:
        linha = input("Inválido, linha do palpite: (0, 1 ou 2)")
        print()

    coluna = input("Coluna do palpite: (0, 1 ou 2) ")
    print()
    
    while coluna not in ["0", "1", "2"]:
        coluna = input("Inválido, coluna do palpite: (0, 1 ou 2)")
        print()

    palpite.append(int(linha))
    palpite.append(int(coluna))
    os.system("cls")

    return palpite

def verificaPalpite(palpite):
    """Verifica se o palpite está em um lugar disponivel e se o jogador acertou o lugar do tesouro"""
    if palpite == tesouro:
        mapa[palpite[0]][palpite[1]] = "💎"
        print("Parabéns, você achou o tesouro!!")
        exibirMapa()
        return "1"

    elif mapa[palpite[0]][palpite[1]] != " ":
        print("Esse espaço já foi usado, tente novamente.")
        exibirMapa()
        return "2"

    else:
        mapa[palpite[0]][palpite[1]] = "X"
        print("Você errou!")
        print()
        exibirMapa()
        return "3"
    
while tentativas >= 1:
    print(f"Você ainda tem {tentativas} tentativas.")
    print()
    tentativa = verificaPalpite(jogada())
    if tentativa == "1":
        break
    elif tentativa == "2":
        input("ENTER para jogar novamente. ")
        print()
    else:
        tentativas -= 1
        input("ENTER para próxima tentativa. ")
        print()