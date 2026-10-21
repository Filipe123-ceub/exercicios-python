import sys

def main():
    # Lê a primeira linha que contém a quantidade de números (N)
    n = int(sys.stdin.readline())
    
    pares = []
    impares = []
    
    # Executa o ciclo N vezes para ler todos os valores
    for _ in range(n):
        valor = int(sys.stdin.readline())
        
        # Verifica se o número é par
        if valor % 2 == 0:
            pares.append(valor)
        else:
            impares.append(valor)
            
    # Ordena a lista de números pares por ordem crescente (comportamento padrão)
    pares.sort()
    
    # Ordena a lista de números ímpares por ordem decrescente
    impares.sort(reverse=True)
    
    # Imprime primeiro todos os pares (um por linha)
    for p in pares:
        print(p)
        
    # De seguida, imprime todos os ímpares (um por linha)
    for i in impares:
        print(i)

if __name__ == "__main__":
    main()