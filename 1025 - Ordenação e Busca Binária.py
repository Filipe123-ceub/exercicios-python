import bisect

def main():
    caso_teste = 1
    
    while True:
        # Lê a primeira linha de cada caso (N e Q).
        # Se houver erro de leitura (ex: linha vazia no final), sai do laço.
        try:
            entrada = input().split()
            if not entrada:
                break
            n = int(entrada[0])
            q = int(entrada[1])
        except EOFError:
            break
            
        # Condição de parada do programa (N=0 e Q=0)
        if n == 0 and q == 0:
            break
            
        print(f"CASE# {caso_teste}:")
        
        # Lê os N números dos mármores
        marmores = []
        for _ in range(n):
            marmores.append(int(input()))
            
        # Ordena a lista de mármores em ordem crescente
        marmores.sort()
        
        # Processa as Q consultas
        for _ in range(q):
            consulta = int(input())
            
            # Utiliza bisect_left para encontrar o índice da PRIMEIRA ocorrência (ou onde deveria estar)
            indice = bisect.bisect_left(marmores, consulta)
            
            # Verifica se o índice retornado é válido e se o número naquela posição é realmente o que buscamos
            if indice < n and marmores[indice] == consulta:
                # Soma 1 porque o problema pede posições começando de 1, e listas em Python começam em 0
                print(f"{consulta} found at {indice + 1}")
            else:
                print(f"{consulta} not found")
                
        # Incrementa o número do caso de teste para a próxima iteração
        caso_teste += 1

if __name__ == "__main__":
    main()