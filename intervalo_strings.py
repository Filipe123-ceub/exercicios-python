import sys

def main():
    # Lê todo o texto de entrada de uma vez e divide-o nas fitas individuais.
    # Isto é ideal para lidar com a exigência de terminar a leitura com EOF.
    entradas = sys.stdin.read().split()
    
    # Se o ficheiro estiver vazio, termina o programa
    if not entradas:
        return
        
    # Dicionário para mapear de forma rápida quem faz par com quem
    pares_validos = {
        'B': 'S',
        'S': 'B',
        'C': 'F',
        'F': 'C'
    }
    
    # Processa cada fita de RNAA lida da entrada
    for fita in entradas:
        pilha = []
        total_ligacoes = 0
        
        # Analisa cada base (letra) da fita individualmente
        for base in fita:
            # Verifica se a pilha não está vazia E se a base atual faz par 
            # com a base que está no topo da pilha (a última que entrou)
            if pilha and pares_validos.get(base) == pilha[-1]:
                # Fazem par! Retiramos a base do topo da pilha (simulando a dobra)
                pilha.pop()
                # Registamos a ligação
                total_ligacoes += 1
            else:
                # Se não fizerem par, a base atual entra na pilha para aguardar o seu par
                pilha.append(base)
                
        # No final da fita, imprimimos o total de ligações formadas
        print(total_ligacoes)

if __name__ == "__main__":
    main()