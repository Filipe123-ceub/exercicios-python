def main():
    primeiro_caso = True
    
    # O programa termina quando encontrar o fim do arquivo (EOF)
    while True:
        try:
            linha = input()
        except EOFError:
            break
            
        # Imprime uma linha em branco APENAS para separar casos de teste
        if not primeiro_caso:
            print()
        primeiro_caso = False
        
        # 1. Contagem das frequências usando um dicionário
        frequencias = {}
        for char in linha:
            if char in frequencias:
                frequencias[char] += 1
            else:
                frequencias[char] = 1
                
        # Converte o dicionário numa lista para podermos ordená-la.
        # Fica no formato: [('A', 3), ('B', 2), ('C', 1)]
        lista_freq = list(frequencias.items())
        
        # 2. A Magia da Ordenação (Duplo Critério)
        # x[0] é o caracter, x[1] é a frequência
        # O sinal negativo (-) inverte a ordem natural, forçando a ordem decrescente
        lista_freq.sort(key=lambda x: (x[1], -ord(x[0])))
        
        # 3. Impressão dos resultados
        for char, freq in lista_freq:
            # ord(char) converte o símbolo no seu número da tabela ASCII
            print(f"{ord(char)} {freq}")

if __name__ == "__main__":
    main()