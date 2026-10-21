import sys

# Função para adicionar criaturas na Árvore de Fenwick 2D
def adicionar(bit, x, y, valor, max_x, max_y):
    i = x
    while i <= max_x:
        j = y
        while j <= max_y:
            bit[i][j] += valor
            # A magia dos bits: salta para o próximo nó responsável por esta área
            j += j & (-j)
        i += i & (-i)

# Função para calcular a soma acumulada de (1,1) até (x,y)
def somar(bit, x, y):
    soma = 0
    i = x
    while i > 0:
        j = y
        while j > 0:
            soma += bit[i][j]
            # Desce na árvore para somar os sub-retângulos
            j -= j & (-j)
        i -= i & (-i)
    return soma

def main():
    linhas = sys.stdin.read().splitlines()
    if not linhas:
        return
        
    idx = 0
    while idx < len(linhas):
        if not linhas[idx].strip():
            idx += 1
            continue
            
        x_str, y_str, p_str = linhas[idx].split()
        max_x = int(x_str)
        max_y = int(y_str)
        preco = int(p_str)
        
        idx += 1
        
        # A entrada termina quando X, Y e P são iguais a 0
        if max_x == 0 and max_y == 0 and preco == 0:
            break
            
        q = int(linhas[idx].strip())
        idx += 1
        
        # Criamos a matriz da BIT. Ela deve ter tamanho X+2 e Y+2 porque
        # a Árvore de Fenwick não lida com o índice 0 (funciona em base 1)
        bit = [[0] * (max_y + 2) for _ in range(max_x + 2)]
        
        for _ in range(q):
            mensagem = linhas[idx].split()
            idx += 1
            tipo = mensagem[0]
            
            if tipo == 'A':
                n = int(mensagem[1])
                # As coordenadas no problema começam em 0
                # Somamos 1 para compatibilidade com a BIT matemática
                px = int(mensagem[2]) + 1
                py = int(mensagem[3]) + 1
                adicionar(bit, px, py, n, max_x, max_y)
                
            elif tipo == 'P':
                x1 = int(mensagem[1]) + 1
                y1 = int(mensagem[2]) + 1
                x2 = int(mensagem[3]) + 1
                y2 = int(mensagem[4]) + 1
                
                # O problema não garante a ordem dos pontos do retângulo.
                # Garantimos que min_x é a esquerda e max_x_q é a direita.
                min_x, max_x_q = min(x1, x2), max(x1, x2)
                min_y, max_y_q = min(y1, y2), max(y1, y2)
                
                # Princípio da Inclusão-Exclusão para a submatriz
                total_schweisen = somar(bit, max_x_q, max_y_q) \
                                  - somar(bit, min_x - 1, max_y_q) \
                                  - somar(bit, max_x_q, min_y - 1) \
                                  + somar(bit, min_x - 1, min_y - 1)
                                  
                # Multiplicamos o total de pragas pelo preço unitário
                custo_total = total_schweisen * preco
                print(custo_total)
                
        # Regra restrita: "Deixe uma linha em branco após cada caso de teste, inclusive após o último"[cite: 20]
        print()

if __name__ == "__main__":
    main()