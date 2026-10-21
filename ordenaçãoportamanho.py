def main():
    # Lê a quantidade de casos de teste (N)
    n = int(input())
    
    # Executa o ciclo N vezes
    for _ in range(n):
        # Lê a linha completa de texto e divide-a numa lista de palavras
        palavras = input().split()
        
        # Ordena a lista:
        # key=len -> O critério de ordenação é o tamanho (length) de cada palavra
        # reverse=True -> Ordena do maior para o menor (ordem decrescente)
        palavras.sort(key=len, reverse=True)
        
        # Junta as palavras ordenadas numa única string separada por espaços
        resultado = " ".join(palavras)
        
        # Imprime o resultado formatado
        print(resultado)

if __name__ == "__main__":
    main()