import os

print("Boa tarde!")
print()
print("Preciso de algumas informações para montar o seu crachá.")
print()

nome = input("Para começar, digite seu nome: ")
os.system("cls")

idade = input("Digite sua idade: ")
os.system("cls")

linguagem = input("Digite a linguagem em que trabalha: ")
os.system("cls")

apelido = input("Digite seu apelido: ")
os.system("cls")

print("-" * 20)
print()
print("🧑‍💻 Crachá do Dev")
print()
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Linguagem: {linguagem}")
print(f"Apelido: {apelido}")
print()
print("-" * 20)