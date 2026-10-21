def main():
    # Lê a quantidade de casos de teste (N)
    n = int(input())
    
    # Executa o ciclo N vezes
    for i in range(n):
        # Lê M (tamanho da tabela) e C (quantidade de chaves)
        linha_mc = input().split()
        m = int(linha_mc[0])
        c = int(linha_mc[1])
        
        # Lê todas as chaves a serem armazenadas e converte para inteiros
        chaves = list(map(int, input().split()))
        
        # Cria a Tabela Hash: uma lista principal contendo M listas vazias no interior
        tabela_hash = [[] for _ in range(m)]
        
        # Processa cada chave lida
        for chave in chaves:
            # Calcula o endereço usando a função de dispersão: h(x) = x mod M
            endereco = chave % m
            
            # Adiciona a chave na lista correspondente àquele endereço (Encadeamento Exterior)
            tabela_hash[endereco].append(chave)
            
        # Formata e imprime o resultado de cada posição da tabela
        for j in range(m):
            # Inicia o texto da linha com "Endereço -> "
            linha_saida = f"{j} -> "
            
            # Adiciona cada chave guardada naquele endereço
            for valor in tabela_hash[j]:
                linha_saida += f"{valor} -> "
                
            # Finaliza a linha com a barra invertida
            linha_saida += "\\"
            
            print(linha_saida)
            
        # Imprime uma linha em branco para separar os casos de teste (excepto no último)
        if i < n - 1:
            print()

if __name__ == "__main__":
    main()