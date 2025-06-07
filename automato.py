

alfabeto = [0,1]
linguagem = ["λ","00","01", "10","11"]
bits = 2

print(f"Alfabeto utilizado: {alfabeto}")
print(f"Palavras: {linguagem}")

def cardinalidade(linguagem, bits):
    contador = 1
    for i in linguagem[1:]:
        if len(i) == bits:
            print(f"A cardinalidade da palavra {contador} é {len(i)}, ")
            contador+=1


def concatenacao(linguagem):
    cont = 1
    for i in linguagem[1:]:
        concat = [i + linguagem[1] ,i + linguagem[2],i + linguagem[3],i + linguagem[4]]
        print(f"Concatenaçõs possíveis com a palavra {cont} {concat} e de cardinalidade {bits * bits}")
        cont+=1  


cardinalidade(linguagem, bits)
concatenacao(linguagem)


