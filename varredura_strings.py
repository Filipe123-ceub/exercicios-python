import sys

def main():
    # Lê todo o arquivo de entrada de uma vez e divide-o pelas quebras de linha.
    # Isto é fundamental para preservar os espaços em branco contínuos da string original.
    linhas = sys.stdin.read().splitlines()
    
    if not linhas:
        return
        
    # A primeira linha contém a quantidade de casos de teste
    n = int(linhas[0])
    
    # Processa cada linha de teste (do índice 1 até N)
    for i in range(1, n + 1):
        if i >= len(linhas):
            break
            
        texto = linhas[i]
        resultado = []
        idx = 0
        
        # Percorre o texto caractere a caractere
        while idx < len(texto):
            char = texto[idx]
            
            # Se for um dos alvos de compactação ('0' ou espaço)
            if char == '0' or char == ' ':
                count = 0
                
                # Conta quantos caracteres iguais existem de forma consecutiva
                while idx < len(texto) and texto[idx] == char:
                    count += 1
                    idx += 1
                    
                # Regra do limite mínimo: só compacta se forem mais de 2
                if count <= 2:
                    resultado.append(char * count)
                else:
                    # Define o símbolo base (# para zeros, $ para espaços)
                    simbolo = '#' if char == '0' else '$'
                    
                    # Regra do limite máximo: divide em blocos de 255
                    while count > 255:
                        resultado.append(simbolo + chr(255))
                        count -= 255
                        
                    # Compacta o que sobrar (ou blocos menores que 255)
                    if count > 0:
                        resultado.append(simbolo + chr(count))
                        
            # Se for uma letra ou número normal, passa direto para o resultado
            else:
                resultado.append(char)
                idx += 1
                
        # Junta a lista final de caracteres numa string contínua e imprime
        print("".join(resultado))

if __name__ == "__main__":
    main()