def main():
    # O problema diz que a entrada termina com o Final de Arquivo (EOF)
    while True:
        try:
            n_str = input()
            # Ignora linhas em branco acidentais que possam existir na plataforma
            if not n_str.strip():
                continue
            n = int(n_str)
        except EOFError:
            break  # Sai do ciclo quando os dados terminarem
            
        telefones = []
        
        # Lê os N números de telefone
        for _ in range(n):
            telefones.append(input().strip())
            
        # O truque de ouro: ordenar a lista para maximizar a economia
        telefones.sort()
        
        economia_total = 0
        
        # Compara cada telefone com o que está logo acima dele na lista ordenada
        for i in range(1, n):
            tel_anterior = telefones[i-1]
            tel_atual = telefones[i]
            
            # Percorre cada caractere (dígito) do telefone
            for j in range(len(tel_atual)):
                if tel_anterior[j] == tel_atual[j]:
                    economia_total += 1
                else:
                    # Assim que um dígito for diferente, o prefixo igual acabou.
                    # Interrompemos este ciclo e passamos para o próximo telefone.
                    break
                    
        # Imprime o resultado do caso de teste atual
        print(economia_total)

if __name__ == "__main__":
    main()