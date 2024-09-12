import datetime #import library manipulation date

nome = input("Qual seu nome: ")
idade = int(input(f"Qual a sua idade {nome}: "))

nascimento = datetime.datetime.now() - idade

print(f"NOME: {nome}")
print(f"IDADE: {idade}")
print(f"NASCIMENTO: {nascimento}")