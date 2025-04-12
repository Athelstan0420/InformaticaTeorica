# Aula 01


Aula 01 - Informática teorica:

---------------------------------------------------------------------------------

    EX: Pense em uma máquina que aceite sequências e caracteres binários que terminam com 0.

        - A máquina aceita como válida apenas senquências que terminam com 0.
        - Se terminar com 1 ela não aceita. 
    
    # Esses principios são os mesmos que fazem a linguagem de programação funcionar. 
    (Compiladores e interpretadores que traduzem os códigos aos computadores.)
---------------------------------------------------------------------------------

    - A informática teórica nos diz se um problema pode ser computável ou não.
    - Problema do caixeiro viajante: 4 cidades, 4 rotas diferentes, Quantas rotas possíveis? E se for 30 cidades ? 

---------------------------------------------------------------------------------
    # Autômatos finitos: (Máquina)
        Composto por...
            #Simbos: 
                -Caracteres com alguma representação: 1,a,y,&,W; 
            #Alfabetos:
                -Conjunto finito e não vazio de simbolos. 
                -Representado por SIGMA Σ.
                -[Strings]: Uma palavra do alfabeto sigma.
                - EX: Σ = {0,1,2,3,4,5,6,7,8,9}
                    palarvras: 123, 987, 1, 41, 1000, etc..
                - O tamanho/(cardinalidade) da palavra é representado por: |p|;
                - Uma palavra vazia/|p| = 0 é representado por: λ(Lambda);
            #Linguagem:
                - Subconjunto de todas as palavras possíveis. 
                - Define quais palavras são "válidas" de um alfabeto sigma, segundo     
                  seu críterio.
                - Regras;
                - Tamanho de uma linguagem: |L|;
        
-------------------------------------------------------------------------------
        
    Exemplo: Lx = {p é uma palavra sobre Σ |p| > 0}

--------------------------------------------------------------------------------

    #Operações básicas:

        - Repetição:

            Operador de repetição como um "expoente"
            EX: 0 com expoente 9 = 000000000;
            EX: K elevado a 0 = λ
            EX: L = {0,1} elevado a 2 -> L = {00,01,10,11}
            EX: L = {a,b} elevado a 3 -> L = {aaa,aab,aba,abb,bbb,bba,bab,baa)
            EX: L = {0,1} elevado a o -> L = {λ}

        - Fecho de Kleen: 
            é representado por/elevado a asterisco, significa "repetido 0 ou + vezes."

            EX: L = {s}* , ou seja, L = {Lambida, s, ss, sss, ssss, sssss,...}
            EX: L = {p pertence {a,b,c} elevado a n | n >= 0}
            - Alfabeto sigma elevado a asterisco = Todas as palavras do alfabeto sigma. 
            EX: [Fecho positivo] de Kleen: (fecho elevado a asterisco - {lambida})
            EX: Se o conjunto L for vazio e o fecho positivo = vazio. 

        - [Concatenação]:
            Palavra formada por os simbolos de uma palavra com outra. 
            Concatenação de Linguagem;
        - [Agrupamento]:
        - [União]: Linguagem que contém todas as palavras de L1 U L2.
        - [interseção]: Linguagem que contém todas as palavras que tem em L1 ^ L2.
        - [Diferença]: Palavras que contém em L1 - L2. 

            
            
---------------------------------------------------------------------------------------------------------------

    
