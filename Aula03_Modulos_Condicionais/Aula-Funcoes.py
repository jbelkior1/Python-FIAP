def print_lyrics(): #FUNÇÃO SEM RETORNO E SEM PARAMETRO

    print("I ain't gonna live forever")
    print("I Just want to live while I'm alive")

print_lyrics()
print_lyrics()

# FUNÇÃO SEM RETORNO E COM PARAMETRO
def boas_vindas (nome):
    print(f"sejá bem-vindo {nome}")

nome_digitado = input("Digite seu nome: ")
boas_vindas (nome_digitado)

# FUNÇÃO COM RETORNO E COM PARAMETRO

def soma(num_a,num_b):
    soma = num_a + num_b
    return soma


resultado_soma = soma(2,5)
print (resultado_soma)