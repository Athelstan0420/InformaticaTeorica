# Aula 01 - Informática teorica:

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
            EX: L = {0,1} elevado a 0 -> L = {λ}

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

# Aula 02 - Info.Teorica:

---------------------------------------------------------
    Um automato reconhece uma liguagem.
---------------------------------------------------------
    
    #Autômatos finitos determinísticos:
        Composto por:
            -Conjunto finito e não vazio de estados.         
            -Único estado a cada instante. 
            -EX: Estado inicial
            -É alimentado por uma palavra de entrada composta por uma sequência de simbolos do alfabeto.
            -Passagem de um estado para outro determinados por regras de transição.
            -Consome cada simbolo da palavra e adota um novo estado pela regra de transição até chegar no seu estado final.
            -Ou seja, consumir toda a palavra. 
 -------------------------------------------------------------------------------------------
    #Definição formal:
     Composto por...
        AFD = É uma quíntupla:  
            - Alfabeto = Sigma
            - Estados = Q
            - Função de transição = δ : Q × Σ → Q
            - Estado inicial = q0 pertencente a Q
            - Estados de aceitação..
-------------------------------------------------------------------------------------

    # Um estado é representado por um circulo com um nome;
    # O estado inicial é identificado por uma seta;
    # O estado final é identificado por bordas duplas; 
    # Um estado pode ser ao mesmo tempo inicial e final; 
    # Uma transição é representada por uma seta -->;

------------------------------------------------------------------------------------
    #Autômatos finitos determinísticos:
        Obrigatótio...
            - Todos os estados tenham uma regra de transição partindo deles para cada um dos simbolos do alfabeto sigma;
            - Não haja mais de uma transição que parte do mesmo estado que consome o mesmo simbolo;
            - Não há obrigação de ter estados finais; 
            - Ter estado inicial;
            
-------------------------------------------------------------------------------------

    #Configuração instantânea:
        - Estado atual e a sequência de simbolos que falta consumir;
        - A configuração A leva á configuração B; Representado pel letra "T" Deitada, com a parte de cima virada para a cinfiguração incial; 
             
---------------------------------------------------------------------------------------------------------------

# Aula 03 Aula 03 info. Teórica:

-------------------------------------------------------------------------
    # Expressões Regulares:
    
        - Ferramentas para expressão de linguagem de maneira compacta; 
        - Uma linguagem é dita uma EXPRESSÃO REGULAR,  se e somente se um AFD reconhece; 
        - Padrões de caracteres que associam sequências de caracteres no texto;
        - 
----------------------------------------------------------------------------------
        # O que não é uma EXPRESSÃO REGULAR:
            - Linguagens não reconhecidas por uma máquina de estados finitos;
            - Linguagens que precisam de memória; 
            - A memória de MEF é muit limitada;
            - MEF não guardam e nem contam cadeias; 
----------------------------------------------------------------------------------

        # Operações em EXPRESSÕES REGULARES:
            - União: {x | x pertence A ^ x pertence a B};
            - Concatenação: {xy | x pertence a A e y pertence a B};
            - Fecho de kleene: {x1, x2, x3... xK | xK >= 0 e cada xI pertence a A}

------------------------------------------------------------------------------------
Info. Teórica - Aula 04: AFN
------------------------------------------------------------------------------------

    Diferentemente do AFD, um AFN permite que, em um determinado estado, 
    com a mesma entrada, a máquina possa transitar para múltiplos estados 
    possíveis. 

    Ou seja, dado um Q existem multiplos próximos Q. Podendo todos serem atingidos de uma só vez. 
    No AFD(Determinítico) existe apenas um próximo Q (Sem escolhas e nem aleatoriedade).
    
    -  ε(épsilon) - AFN = {Q, Σ(sigma), q0, δ(Delta), F}
    -  δ = QxΣUε -> 2elevado a Q.
    -  TODOS OS ESTADOS TEM UMA TRANSIÇÃO EPSILON PARA SI MESMO.  

    PARA CONSTRUIR UM AFN É NECESSÁRIO PENSAR APENAS NA SOLUÇÃO PARA O AUTÔMATO ACEITAR A PALAVRA;

   
------------------------------------------------------------------------------------    
Info. Teórica - Aula 05: CONVERSAO DE AFN P/ AFD
------------------------------------------------------------------------------------
    - Todo AFD é um AFN, mas a recíproca não é vdd. 
    - Existe um AFD equivalente para cada AFN. 

    - Passo a passo p/ conversão:
        Traduzir p/ notação tabular:
            Construir tabela:
                1. linha: todos os  estados. (A,B);
                2. colunas: símbolos do alfabeto. (0,1);
                

------------------------------------------------------------------------------------    
Info. Teórica - Aula 06: EQUIVALÊNCIA DE AUTÔMATOS
------------------------------------------------------------------------------------

    - São aqueles que reconhecem a mesma linguagem formal. Para tal cadeia de entrada, ambos os autômatos a aceitarão ou rejeitarão consistentemente. 

    Regras para identificar equivalência:

        1. Os dois autômatos não serão equivalntes se o par {qa, qb} um for estado final e o outro não.
        2. Se o estado inicial de um for final, então, no segundo, o estado inicial tabém terá que ser final para seram equivalentes. 

------------------------------------------------------------------------------------    
Info. Teórica - Aula 07: LEMA DO BOMBEAMENTO
------------------------------------------------------------------------------------

    ------------------------------------------------------------------------------------
    - SERVE PARA PROVAR QUE UMA LINGUAGEM NÃO É REGULAR,
    - ou seja, que não pode ser reconhecida por um autômato finito,
    - MAS NÃO PROVA QUE UMA LINGUAGEM É REGULAR.
    ------------------------------------------------------------------------------------
    
    Se uma linguagem L é regular, então existe um número inteiro p(chamado de constante de bombeamento) tal que qualquer palavra w em L com comprimento ∣w∣ ≥ p pode ser dividida em três partes:
    
                                                                           w=xyz
    de forma que:
    
        1. ∣xy∣ ≤ p
        (A parte xy está dentro dos primeiros p caracteres de w)
    
        2. ∣y∣ ≥ 1
        (A parte y não pode ser vazia)
    
        3. Para todo i ≥ 0, xyELEVADO(i)z ∈ L
        (Se você repetir o bloco y qualquer número de vezes — até 0 vezes — o resultado ainda deve estar em L)

    ------------------------------------------------------------------------------------

    COMO É USADO ?
    
        Suponha que a linguagem é regular. 
        Pelo lema, existe um valor p. (valor qualquer, só precisa ser maior que o número de estados de um AFD qualquer)
        Pegue uma palavra w∈L tal que ∣w∣ ≥ p.
        Mostre que para toda divisão de w=xyz que satisfaça as condições 1 e 2, existe algum i tal que xyELEVADOA(i)z∉L.
        Isso contradiz o lema, então L não é regular.

        OBS: "i" significa quantas vezes o trecho vai se repetir; 
    ------------------------------------------------------------------------------------

    (EX:)
        
        - p=3 (valor qualquer, só precisa ser maior que o número de estados de um AFD qualquer);
        - Pegue a palavra w=aaabbb ∈ L (tem 6 letras ≥ 3);
        - Segundo o lema, podemos dividir: w=xyz
        
        Com:
    
            ∣xy∣≤ p→ ou seja, x e y estão dentro de aaa;      
            ∣y∣≥1∣y∣≥1 → yy não pode ser vazio;

        - Exemplo de divisão:

            x= a
            y= a
            z= abbb
            → w = xyz=a+a+abbb= aaabbb

        - Agora testamos:
        
            xy0z= xz=aabbb∈L       
            xy2z= aa+a+abbb=aaaabbb∈L        
            xy3z= aaaabbb∈L
    ------------------------------------------------------------------------------------

------------------------------------------------------------------------------------    
Info. Teórica - Aula 08: GRAMÁTICAS REGULARES
------------------------------------------------------------------------------------

    # MODELO DE GRAMÁTICA DE NOAM CHOMSKY:
    
    TIPO - GRAMÁTICA ACEITA - LINGUAGEM ACEITA - AUTÔMATO:
    
        - Tipo 0 =  irrestrita =  Recursivamente Enumeráveis = Máquina de Turing;
        
        - Tipo 1 =  sensível ao contexto;
        
        - Tipo 2 =  livre de contexto (GLC) = Livres de Contexto	Autômato = com Pilha(PDA);
        
        - Tipo 3 =	 regular =  Regulares = Autômato Finito (AFD/AFN);
    ------------------------------------------------------------------------------------

    G.R = (V,T,S,P)
    
    - G.R. são divididas em dois tipos:
        1. LINEAR DIREITA (A -> xB);
        2. LINEAR ESQUERDA (A -> Bx);
        
    - Derivação de uma gramática:
        Conjunto de todas as cadeias que podem ser derivadas de uma gramática é chamada de linguagem gerada pela gramática;

    ------------------------------------------------------------------------------------
