import math

def main():
    # Lê a primeira linha indicando a quantidade de casos de teste (N)
    n = int(input())
    
    for _ in range(n):
        # Lê a linha inteira e separa-a pelos espaços em branco
        linha = input().split()
        
        # Extrai as variáveis baseando-se nos seus índices na lista
        n1 = int(linha[0])
        # linha[1] é sempre a barra '/', não precisamos de a guardar
        d1 = int(linha[2])
        op = linha[3]
        n2 = int(linha[4])
        # linha[5] é sempre a barra '/', não precisamos de a guardar
        d2 = int(linha[6])
        
        # Variáveis para guardar o resultado da fração antes da simplificação
        num_res = 0
        den_res = 0
        
        # Aplica a fórmula matemática correta consoante o operador lido
        if op == '+':
            num_res = (n1 * d2) + (n2 * d1)
            den_res = (d1 * d2)
        elif op == '-':
            num_res = (n1 * d2) - (n2 * d1)
            den_res = (d1 * d2)
        elif op == '*':
            num_res = (n1 * n2)
            den_res = (d1 * d2)
        elif op == '/':
            num_res = (n1 * d2)
            den_res = (n2 * d1)
            
        # Calcula o Máximo Divisor Comum (MDC) para simplificar a fração
        mdc = math.gcd(num_res, den_res)
        
        # Calcula os valores finais simplificados usando divisão inteira (//)
        simp_num = num_res // mdc
        simp_den = den_res // mdc
        
        # Imprime o resultado formatado conforme exigido pelo problema
        print(f"{num_res}/{den_res} = {simp_num}/{simp_den}")

if __name__ == "__main__":
    main()