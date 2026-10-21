def main():
    # Lê a primeira linha com o número total de casos de teste (N)
    n = int(input())
    
    # Executa o ciclo N vezes, uma para cada caso de teste
    for _ in range(n):
        mina = input()
        
        pedacos_esquerdos = 0
        diamantes_extraidos = 0
        
        # Analisa cada partícula da mina (caractere da linha)
        for particula in mina:
            if particula == '<':
                # Encontrou a metade esquerda do diamante
                pedacos_esquerdos += 1
                
            elif particula == '>':
                # Encontrou a metade direita. Vamos ver se temos a metade esquerda correspondente!
                if pedacos_esquerdos > 0:
                    diamantes_extraidos += 1   # Formámos um diamante!
                    pedacos_esquerdos -= 1     # Retiramos a metade esquerda usada
                    
            # Se a partícula for '.', o código simplesmente não faz nada (ignora a areia)
            
        # Imprime o total de diamantes encontrados nesta mina
        print(diamantes_extraidos)

if __name__ == "__main__":
    main()