import sys

def main():
    # Lemos toda a entrada de uma vez e dividimos em "palavras/tokens".
    # Isto é à prova de falhas contra espaços extra ou linhas em branco na plataforma.
    dados = sys.stdin.read().split()
    if not dados:
        return
        
    idx = 0
    while idx < len(dados):
        # A primeira linha do caso de teste contém o número total de vagões (N)
        n = int(dados[idx])
        idx += 1
        
        # A última linha contém apenas 0, indicando o fim da entrada
        if n == 0:
            break
            
        # Extrai a sequência de vagões que vêm do lado A
        A = dados[idx : idx + n]
        idx += n
        
        # Extrai a sequência desejada pelo chefe para o lado B
        B = dados[idx : idx + n]
        idx += n
        
        pilha = []
        movimentos = []
        idx_a = 0
        idx_b = 0
        impossivel = False
        
        # O ciclo corre até conseguirmos preencher todos os N vagões na linha B
        while idx_b < n:
            # 1ª Tentativa: O vagão que precisamos está na ponta da estação (topo da pilha)?
            # pilha[-1] em Python acede rapidamente ao último elemento da lista
            if pilha and pilha[-1] == B[idx_b]:
                pilha.pop()             # Tira o vagão da estação
                movimentos.append('R')  # Regista o movimento de Remover
                idx_b += 1              # Avança para o próximo vagão que precisamos em B
                
            # 2ª Tentativa: Se não está na ponta, podemos ir buscar mais à linha A?
            elif idx_a < n:
                pilha.append(A[idx_a])  # Empurra o vagão da linha A para a estação
                movimentos.append('I')  # Regista o movimento de Inserir
                idx_a += 1              # Avança para o próximo vagão disponível em A
                
            # 3º Cenário: Não temos o vagão na ponta e já não há mais vagões em A. Estamos bloqueados!
            else:
                impossivel = True
                break
                
        # Junta todas as letras 'I' e 'R' numa única string de texto sem espaços
        resultado = "".join(movimentos)
        
        # Se as operações foram interrompidas, acrescenta " Impossible" com um espaço antes
        if impossivel:
            resultado += " Impossible"
            
        print(resultado)

if __name__ == "__main__":
    main()