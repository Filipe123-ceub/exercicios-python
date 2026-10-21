def main():
    primeiro_caso = True
    
    while True:
        # Lê a quantidade de camisetas (N)
        try:
            n_str = input().strip()
            if not n_str:
                continue
            n = int(n_str)
        except EOFError:
            break
            
        # A entrada termina quando N for igual a zero
        if n == 0:
            break
            
        # Imprime uma linha em branco ENTRE os casos de teste
        if not primeiro_caso:
            print()
        primeiro_caso = False
        
        camisetas = []
        
        # Lê os dados das N camisetas
        for _ in range(n):
            # A primeira linha contém o nome
            nome = input().strip()
            
            # A segunda linha contém a cor e o tamanho separados por espaço
            detalhes = input().strip().split()
            cor = detalhes[0]
            tamanho = detalhes[1]
            
            # Guarda os dados num dicionário
            camisetas.append({'nome': nome, 'cor': cor, 'tamanho': tamanho})
            
        # O Segredo: Ordenação com 3 critérios simultâneos
        # 1º: x['cor'] -> Ordem alfabética ascendente (branco > vermelho)
        # 2º: -ord(x['tamanho']) -> Ordem alfabética descendente (P > M > G)
        # 3º: x['nome'] -> Ordem alfabética ascendente para desempatar nomes
        camisetas.sort(key=lambda x: (x['cor'], -ord(x['tamanho']), x['nome']))
        
        # Imprime a saída formatada "cor tamanho nome"
        for c in camisetas:
            print(f"{c['cor']} {c['tamanho']} {c['nome']}")

if __name__ == "__main__":
    main()