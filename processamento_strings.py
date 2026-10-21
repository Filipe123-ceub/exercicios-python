import sys

def main():
    while True:
        try:
            # Lê a linha e separa os quatro valores
            linha = input().split()
            
            # Condição de segurança caso haja linhas vazias indesejadas
            if not linha:
                continue
                
            x1, y1, x2, y2 = map(int, linha)
            
        except EOFError:
            break
            
        # O final da entrada é indicado por uma linha contendo quatro zeros
        if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
            break
            
        # Avalia a quantidade de movimentos necessários
        if x1 == x2 and y1 == y2:
            # O destino é a mesma casa de partida
            print(0)
        elif x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
            # O destino está na mesma linha, coluna ou diagonal
            print(1)
        else:
            # Qualquer outro destino num tabuleiro vazio demora exatamente 2 passos
            print(2)

if __name__ == "__main__":
    main()