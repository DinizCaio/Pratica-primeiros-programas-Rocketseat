import os

print("Boa tarde! Sou o ORÁCULO da sabedoria")
print()

linguagem = input("Sobre qual linguagem de programação deseja aprender? (python, html, css, javascript) ").lower()

os.system("cls")

match linguagem:
    case "python":
        print("Python é uma linguagem de programação de alto nível, simples e fácil de aprender, criada por Guido van Rossum e lançada em 1991.")
    case "html" :
        print("HTML (HyperText Markup Language) não é uma linguagem de programação, mas sim uma linguagem de marcação usada para estruturar o conteúdo das páginas da web.")
    case "css" :
        print("CSS (Cascading Style Sheets) é a linguagem usada para estilizar páginas web feitas com HTML.")
    case "javascript" :
        print("JavaScript (JS) é uma linguagem de programação usada principalmente para criar interatividade em páginas web.")
    case _ :
        print("Desculpa, não entendi!")
    
print()
print("Até a próxima!")