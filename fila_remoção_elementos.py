import sys
from collections import deque
import heapq

def main():
    # O final da entrada é determinado pelo final do arquivo (EOF).
    # Lemos tudo de uma vez para ser mais rápido e ignorar quebras de linha irregulares.
    dados = sys.stdin.read().split()
    if not dados:
        return
        
    idx = 0
    total_elementos = len(dados)
    
    while idx < total_elementos:
        # Lê a quantidade de comandos do caso de teste (n)
        n = int(dados[idx])
        idx += 1
        
        # Flag para manter o controlo das hipóteses possíveis
        hipotese_stack = True
        hipotese_queue = True
        hipotese_pq = True
        
        # Inicializa as três estruturas de dados para simulação
        pilha = []
        fila = deque()
        fila_prioridade = []
        
        # Processa as 'n' linhas de comandos deste caso de teste
        for _ in range(n):
            comando = int(dados[idx])
            valor = int(dados[idx+1])
            idx += 2
            
            if comando == 1:
                # Comando 1: Joga um elemento na sacola
                if hipotese_stack:
                    pilha.append(valor)
                if hipotese_queue:
                    fila.append(valor)
                if hipotese_pq:
                    # O heapq em Python é um "Min-Heap" (menores primeiro).
                    # Para virar um "Max-Heap" (maiores primeiro), inserimos o valor negativo.
                    heapq.heappush(fila_prioridade, -valor)
                    
            elif comando == 2:
                # Comando 2: Tira um elemento da sacola
                
                # Teste da Pilha (LIFO)
                if hipotese_stack:
                    if not pilha or pilha.pop() != valor:
                        hipotese_stack = False
                        
                # Teste da Fila (FIFO)
                if hipotese_queue:
                    # popleft() retira rapidamente o elemento do início (o mais antigo)
                    if not fila or fila.popleft() != valor:
                        hipotese_queue = False
                        
                # Teste da Fila de Prioridade (Maiores primeiro)
                if hipotese_pq:
                    # Como inserimos negativo, tiramos o valor e voltamos a multiplicar por -1
                    if not fila_prioridade or -heapq.heappop(fila_prioridade) != valor:
                        hipotese_pq = False
                        
        # Após avaliar o caso de teste, somamos as hipóteses que ainda são verdadeiras
        hipoteses_restantes = hipotese_stack + hipotese_queue + hipotese_pq
        
        # Classifica a saída de acordo com o exigido pelo problema
        if hipoteses_restantes == 0:
            print("impossible")
        elif hipoteses_restantes > 1:
            print("not sure")
        elif hipotese_stack:
            print("stack")
        elif hipotese_queue:
            print("queue")
        elif hipotese_pq:
            print("priority queue")

if __name__ == "__main__":
    main()