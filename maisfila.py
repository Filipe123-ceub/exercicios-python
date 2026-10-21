def main():
    while True:
        # Lê a quantidade de crianças e verifica a condição de paragem (0)
        n = int(input())
        if n == 0:
            break
            
        roda = []
        # Constrói a roda inicial com o Nome e o Valor da ficha
        for _ in range(n):
            entrada = input().split()
            nome = entrada[0]
            valor = int(entrada[1])
            # Guardamos os dados de cada criança num dicionário dentro da lista
            roda.append({'nome': nome, 'valor': valor})
            
        indice_atual = 0
        valor_ficha = roda[indice_atual]['valor']
        
        # --- PRIMEIRA ELIMINAÇÃO ---
        # Como o tamanho da lista ainda não mudou, calculamos o alvo diretamente
        if valor_ficha % 2 != 0:
            # Ficha Ímpar: sentido anti-horário (avança)
            alvo = (indice_atual + valor_ficha) % len(roda)
        else:
            # Ficha Par: sentido horário (recua)
            alvo = (indice_atual - valor_ficha) % len(roda)
            
        # Guarda o valor da ficha da criança que vai ser eliminada
        valor_ficha = roda[alvo]['valor']
        # Remove a criança da roda
        roda.pop(alvo)
        # O novo ponto de partida é o buraco deixado pela criança eliminada
        indice_atual = alvo
        
        # --- RESTANTES ELIMINAÇÕES ---
        # O ciclo continua até sobrar apenas uma criança (a vencedora)
        while len(roda) > 1:
            if valor_ficha % 2 != 0:
                # Ímpar: desconta-se 1 porque a lista encolheu para a esquerda
                alvo = (indice_atual + valor_ficha - 1) % len(roda)
            else:
                # Par: recuar mantém a matemática inalterada
                alvo = (indice_atual - valor_ficha) % len(roda)
                
            valor_ficha = roda[alvo]['valor']
            roda.pop(alvo)
            indice_atual = alvo
            
        # Imprime o resultado final respeitando o formato exigido (com o espaço após os dois pontos)
        print(f"Vencedor(a): {roda[0]['nome']}")

if __name__ == "__main__":
    main()