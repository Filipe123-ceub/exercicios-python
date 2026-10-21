from collections import deque

def main():
    while True:
        # Lê o número n
        n = int(input())
        
        # A última linha contém 0 e não deve ser processada
        if n == 0:
            break
            
        # Cria a fila (deque) com as cartas enumeradas de 1 até n
        cartas = deque(range(1, n + 1))
        descartadas = []
        
        # A operação é realizada enquanto tiver 2 ou mais cartas na pilha
        while len(cartas) >= 2:
            # 1. Joga fora a carta do topo (remove do início e guarda na lista de descartadas)
            carta_descartada = cartas.popleft()
            descartadas.append(carta_descartada)
            
            # 2. Mova a próxima carta para a base da pilha (remove do início e insere no fim)
            carta_movida = cartas.popleft()
            cartas.append(carta_movida)
            
        # Prepara a formatação da saída para ficar exatamente como o problema pede
        # O map(str, descartadas) converte os números em texto
        # O ", ".join(...) junta tudo separado por vírgula e espaço
        str_descartadas = ", ".join(map(str, descartadas))
        
        # Imprime as duas linhas requeridas
        print(f"Discarded cards: {str_descartadas}")
        print(f"Remaining card: {cartas[0]}")

if __name__ == "__main__":
    main()