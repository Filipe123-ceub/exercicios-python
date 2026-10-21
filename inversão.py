def main():
    # Lê a primeira linha que contém o número de casos de teste (N)
    n = int(input())
    
    # Executa o ciclo N vezes, uma para cada caso de teste
    for _ in range(n):
        # Lê o tamanho do comboio (L)
        l = int(input())
        
        # Se o tamanho do comboio for 0, não há trocas a fazer
        if l == 0:
            print("Optimal train swapping takes 0 swaps.")
            continue
            
        # Lê a ordem atual dos vagões e transforma-os numa lista de números inteiros
        vagoes = list(map(int, input().split()))
        
        swaps = 0
        
        # Conta o número de inversões (quantas vezes um número maior aparece antes de um menor)
        for i in range(l):
            for j in range(i + 1, l):
                # Se o vagão na posição i for maior que um vagão que está mais à frente (posição j)
                if vagoes[i] > vagoes[j]:
                    swaps += 1
                    
        # Imprime o resultado com a formatação exata pedida no enunciado
        print(f"Optimal train swapping takes {swaps} swaps.")

if __name__ == "__main__":
    main()