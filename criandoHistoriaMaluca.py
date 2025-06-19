import os

print("Vamos jogar um MADLIB!")
print()

sabeJogar = input("Você sabe jogar MADLIB? (s/n): ")
print()

if sabeJogar.lower() == "s":
    print("Vamos ao jogo!")
else:
    print("Não? Então vou pedir algumas palavras, e com elas vou formar uma história engraçada!")

input("Aperte ENTER para começar.")
os.system("cls")

lugar = input("Digite um lugar: ")
os.system("cls")

famoso = input("Digite o nome de alguem famoso: ")
os.system("cls")

objeto = input("Digite um objeto qualquer: ")
os.system("cls")

cor = input("Digite uma cor: ")
os.system("cls")

verbo = input("Digite um verbo: ")
os.system("cls")

numero = input("Digite um número: ")
os.system("cls")

input("Aperte ENTER para gerar sua história!")
os.system("cls")

print(f"Em um belo dia, estava no(a) {lugar}, quando derrepente o {famoso} chegou.")
print(f"Por incrível que pareça, ele estava {verbo} um {objeto} {cor}.")
print(f"O estranho é que isso durou {numero} horas.")