import sys

def main():
    # Lê todas as linhas da entrada de uma só vez para ser mais rápido
    linhas = sys.stdin.read().splitlines()
    if not linhas:
        return
        
    # A primeira linha da entrada contém um valor inteiro N, que indica o número de casos de teste
    n = int(linhas[0])
    
    # Dicionário para definir a prioridade de cada operador matemático
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    
    # Processa cada caso de teste (da linha 1 até N)
    for i in range(1, n + 1):
        if i >= len(linhas):
            break
            
        expressao_infixa = linhas[i]
        resultado_posfixo = []
        pilha_operadores = []
        
        for char in expressao_infixa:
            # Se for um número ou letra, vai direto para a saída pós-fixa
            if char.isalnum():
                resultado_posfixo.append(char)
                
            # Se for parêntese de abrir, vai para a pilha
            elif char == '(':
                pilha_operadores.append(char)
                
            # Se for parêntese de fechar, esvazia a pilha para o resultado até encontrar o de abrir
            elif char == ')':
                while pilha_operadores and pilha_operadores[-1] != '(':
                    resultado_posfixo.append(pilha_operadores.pop())
                # Remove o '(' da pilha e descarta-o
                if pilha_operadores and pilha_operadores[-1] == '(':
                    pilha_operadores.pop()
                    
            # Se for um operador matemático
            else:
                # Verifica a precedência para decidir se o novo operador "empurra" os antigos para a saída
                while pilha_operadores and pilha_operadores[-1] != '(':
                    operador_topo = pilha_operadores[-1]
                    
                    # Se o topo tiver precedência maior ou igual, tem de sair primeiro
                    if precedencia.get(operador_topo, 0) >= precedencia.get(char, 0):
                        resultado_posfixo.append(pilha_operadores.pop())
                    else:
                        break
                        
                # Coloca o operador atual na pilha
                pilha_operadores.append(char)
                
        # No final da expressão, esvazia quaisquer operadores que tenham sobrado na pilha
        while pilha_operadores:
            resultado_posfixo.append(pilha_operadores.pop())
            
        # Junta a lista de caracteres numa string contínua e imprime o resultado
        print("".join(resultado_posfixo))

if __name__ == "__main__":
    main()