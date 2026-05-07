apelidos = ['Joao' , 'Maria', 'Rodiney', 'Carlos']

for i in range (len(apelidos)):
    for j in range(i+1, len(apelidos)):
        print (apelidos[i],apelidos[j])

print()
print()

for i in range (len(apelidos)):
    for j in range(len(apelidos)):
        if i != j:
            print(apelidos[j] , apelidos[i])
        else:
            break

