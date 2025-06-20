import os

perguntas = [
    ["Qual é o maior país do mundo em extensão territorial?", "russia"],
    ["Quem pintou a obra Mona Lisa?", "leonardo da vinci"],
    ["Em que ano o homem pisou na lua pela primeira vez?", "1969"],
    ["Quantos elementos existem na tabela periódica?", "118"],
    ["Quem foi o primeiro presidente do Brasil?", "deodoro da fonseca"],
    ["Qual é a capital do Canadá?", "ottawa"],
    ["Quantos ossos tem o corpo humano adulto?", "206"],
    ["Quem escreveu Dom Casmurro?", "machado de assis"],
    ["Qual país sediou a Copa do Mundo de futebol de 2022?", "catar"],
    ["Qual é o maior planeta do sistema solar?", "jupiter"]
]

acertos = 0

print("Esse é o show do milhão!")
print()
print("Farei perguntas de conhecimentos gerais e no final, de acordo com a sua pontuação, receberá um prêmio")
print()
input("Para começar aperte ENTER")

for i in range (len(perguntas)):
    os.system("cls")
    print(f"Pergunta {i + 1}:")
    print()
    resposta = input(f"{perguntas[i][0]} ").lower()
    if resposta == perguntas[i][1]:
        os.system("cls")
        acertos += 1
        print("Parabéns, resposta correta!")
        if i < 9:
            input("Aperte ENTER para a próxima pergunta.")
        else:
            input("Aperte ENTER para encerrar")
    else:
        os.system("cls")
        print("Resposta incorreta!")
        if i < 9:
            input("Aperte ENTER para a próxima pergunta.")
        else:
            input("Aperte ENTER para encerrar")

premio = 1000 * (2**acertos)

os.system("cls")
print("Este foi o Show do Milhão")
print()
print(f"Você teve {acertos} respostas corretas!")
print()
input("Para revelar seu prêmio, aperte ENTER")

os.system("cls")
print(f"Seu prêmio é de R$ {premio}")
print()
print("Obrigado por participar!")