def main():
    while True:
        # Lê a linha e separa os três valores de N, k e m
        try:
            linha = input().split()
            if not linha:
                continue
            n = int(linha[0])
            k = int(linha[1])
            m = int(linha[2])
        except EOFError:
            break
            
        # Condição de paragem exigida (0 0 0)
        if n == 0 and k == 0 and m == 0:
            break
            
        # Cria o círculo de candidatos (lista de 1 até N)
        # 0 significará que o candidato já foi retirado
        candidatos = list(range(1, n + 1))
        
        # p1 (sentido horário): começa um índice ANTES do primeiro, para que o 1º passo calhe no índice 0
        p1 = -1  
        # p2 (sentido anti-horário): começa um índice APÓS o último, para que o 1º passo calhe no índice n-1
        p2 = n   
        restantes = n
        
        resultado = []
        
        # O processo continua até que não reste ninguém
        while restantes > 0:
            
            # Movimento do funcionário 1 (sentido horário, k posições)
            passos_p1 = 0
            while passos_p1 < k:
                p1 = (p1 + 1) % n           # Avança 1 casa de forma circular
                if candidatos[p1] != 0:     # Se houver lá um candidato válido...
                    passos_p1 += 1          # ...conta como um passo
                    
            # Movimento do funcionário 2 (sentido anti-horário, m posições)
            passos_p2 = 0
            while passos_p2 < m:
                p2 = (p2 - 1 + n) % n       # Recua 1 casa de forma circular
                if candidatos[p2] != 0:     # Se houver lá um candidato válido...
                    passos_p2 += 1          # ...conta como um passo
                    
            # Verificação das Escolhas
            if p1 == p2:
                # Escolheram a mesma pessoa. Imprime o número usando formatação de 3 casas
                resultado.append(f"{candidatos[p1]:>3}")
                candidatos[p1] = 0          # Marca como removido
                restantes -= 1              # Saiu 1 pessoa
            else:
                # Escolheram pessoas diferentes. Imprime os dois com 3 casas cada
                resultado.append(f"{candidatos[p1]:>3}{candidatos[p2]:>3}")
                candidatos[p1] = 0          # Marca o 1º como removido
                candidatos[p2] = 0          # Marca o 2º como removido
                restantes -= 2              # Saíram 2 pessoas
                
        # Junta os pares guardados separando-os apenas com uma vírgula
        print(",".join(resultado))

if __name__ == "__main__":
    main()