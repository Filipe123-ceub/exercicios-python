def main():
    # O laço roda continuamente lendo as N expressões até o fim do arquivo (EOF)
    while True:
        try:
            expressao = input()
        except EOFError:
            break
            
        contador = 0
        erro = False
        
        # Analisa cada letra/símbolo da expressão lida
        for caractere in expressao:
            if caractere == '(':
                contador += 1
            elif caractere == ')':
                if contador > 0:
                    contador -= 1
                else:
                    # Encontrou um ')' mas o contador é 0, ou seja, não há um '(' para ele.
                    erro = True
                    break # Interrompe a análise desta linha, pois já sabemos que está errada
                    
        # Verificação Final da expressão
        # Para ser "correct", não pode ter acionado o erro e o contador deve terminar zerado
        if not erro and contador == 0:
            print("correct")
        else:
            print("incorrect")

if __name__ == "__main__":
    main()