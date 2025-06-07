

alfabeto = [0,1]
linguagem = ["λ","00","01", "10","11"]
bits = 2

print(f"Alfabeto utilizado: {alfabeto}")
print(f"Palavras: {linguagem}")

def cardinalidade(linguagem):
    contador = 1
    for i in linguagem[1:]:
        print(f"A cardinalidade da palavra {contador} é {len(i)}, ")
        contador+=1


def concatenacao(linguagem):
    a = []
    c = 1
    for i in linguagem[1:]:
        concat = [i + linguagem[1] ,i + linguagem[2],i + linguagem[3],i + linguagem[4]]
        for i in concat:
            # print(i)
            a.append(i)
        print(f"Concatenaçõs possíveis com a palavra {linguagem[c]} {concat} e de cardinalidade {bits * bits}")
        c+=1
    # print(a)



# cardinalidade(linguagem)
concatenacao(linguagem)



