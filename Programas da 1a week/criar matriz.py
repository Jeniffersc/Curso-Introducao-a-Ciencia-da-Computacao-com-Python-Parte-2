def cria_matriz(num_linhas, num_colunas, valor):
    '''(int, int, int) -> matriz (lista de listas)
    Cria e retorna uma matriz com num_linhas linhas e num_colunas colunas
    colunas em que cada elemento é igual ao valor dado
    '''
    matriz = [] #criar lista vazia - Guarda as linhas da matriz
    
    for i in range(num_linhas): # O for vai ser repetido até o valor de num_linhas
        #cria a linha i
        linha = [] #cria lista vazia
        for j in range(num_colunas): # O for vai ser repetido até o valor de num_colunas
            linha.append(valor) # Função append acrescenta o valor passado como parâmetro no final da linha

        #Adiciona linha à matriz
            matriz.append(linha) # Função append acrescenta a linha à matriz 

        return matriz
