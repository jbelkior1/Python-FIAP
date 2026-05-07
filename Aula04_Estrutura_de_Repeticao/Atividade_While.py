
nota1 = float(input("Digite a primeira nota: "))
while nota1 < 0 or nota1 > 10:
    print("Anota deve ser de 0 a 10")
    nota1 = float(input("Digite a primeira nota novamente: "))

nota2 = float(input("Digite a segunda a nota: "))
while nota2 < 0 or nota2 > 10:
    print("Anota deve ser de 0 a 10")
    nota2 = float(input("Digite a primeira nota novamente: "))

media = (nota1 + nota2) / 2
print (media)



