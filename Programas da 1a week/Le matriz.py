def cria_matriz(num_linhas, num_colunas):
    '''(int, int, int) -> matriz (lista de listas)
    Cria e retorna uma matriz com num_linhas linhas e num_colunas colunas
    colunas em que cada elemento é digitado pelo usuário
    '''
    matriz = [] #criar lista vazia - Guarda as linhas da matriz
    
    for i in range(num_linhas): # O for vai ser repetido até o valor de num_linhas
        #cria a linha i
        linha = [] #cria lista vazia
        for j in range(num_colunas): # O for vai ser repetido até o valor de num_colunas
            valor = int(input("Digite o elemento [" + str(i) + "][" + str (j) + "]")) #Solicita para o usuário digitar o elemento da linha i e coluna j (transforma o i e j numerico's para uma string's)
            linha.append(valor) #Adiciona o valor no finla da linha
            
        #Adiciona linha à matriz
        matriz.append(linha) # Função append acrescenta a linha à matriz 

    return matriz

def le_matriz():
    lin = int(input("Digite o número de linhas da matriz: "))
    col = int(input("Digite o número de colunas da matriz: "))
    return cria_matriz(lin, col)
