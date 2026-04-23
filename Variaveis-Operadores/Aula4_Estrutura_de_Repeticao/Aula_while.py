#Contador de Produtos While Crescente
print("Exemplo 1")
print()
cp = 0
while cp < 3:
    print(f"Produto {cp}")
    cp += 1

#Contador de Produtos While decrescente 4 a 1
print()
print("Exemplo 2")
print()
i = 4
while i  > 0:
    print(f"Produto {i}")
    i   -= 1

#Contador de Produtos While
''' 
print()
print("Exemplo 3")
print()

jogar = "Sim"

while jogar.lower() == "sim":
    print("Repete o jogo")
    jogar = input("Deseja jogar novamente?")
'''

#Contador de Produtos While continue (modificador de fluxo)
print()
print("Exemplo 4")
print()

i = 0
while i < 10:
    i += 1

    if i == 3:
        continue

    print (f"Produto {i}")

#Contador de Produtos While break (modificador de fluxo)

print()
print("Exemplo 5")
print()

i = 0
while i < 10:
    i += 1

    if i == 5 or i == 9:
        break

    print (f"Produto {i}")

# Contador de Produtos While decrescente com input

print()
print("Exemplo 5")
print()

n = int(input("Digite o valor: "))
v = 1

while v <= n:
    print(v)
    v +=1