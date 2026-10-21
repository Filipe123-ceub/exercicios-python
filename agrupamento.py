import sys

def main():
    # 1. Leitura supersónica: lê todo o texto de entrada de uma vez e divide em palavras/números
    dados = sys.stdin.read().split()
    if not dados:
        return
        
    idx = 0
    cidade_num = 1
    
    while idx < len(dados):
        # Lê o N (número de imóveis)
        n = int(dados[idx])
        idx += 1
        
        # Condição de paragem
        if n == 0:
            break
            
        # Imprime uma linha em branco para separar os casos (mas não antes do primeiro)
        if cidade_num > 1:
            print()
            
        print(f"Cidade# {cidade_num}:")
        
        total_pessoas = 0
        total_consumo = 0
        
        # 2. O Algoritmo de "Gavetas" (Counting Sort)
        # Cria 201 gavetas (índices de 0 a 200) todas a zeros
        pessoas_por_consumo = [0] * 201
        
        for _ in range(n):
            x = int(dados[idx])
            y = int(dados[idx+1])
            idx += 2
            
            total_pessoas += x
            total_consumo += y
            
            # Consumo individual arredondado para baixo usando divisão inteira
            consumo_individual = y // x
            
            # Adiciona a quantidade de pessoas à gaveta correta
            pessoas_por_consumo[consumo_individual] += x
            
        # 3. Formatação da Saída das Pessoas/Consumo
        saida_consumos = []
        for consumo in range(201):
            if pessoas_por_consumo[consumo] > 0:
                saida_consumos.append(f"{pessoas_por_consumo[consumo]}-{consumo}")
                
        # Junta tudo na mesma linha, separado por espaços
        print(" ".join(saida_consumos))
        
        # 4. Cálculo da Média "Sem Arredondamento" (Truncagem Matemática)
        # Exemplo: total = 186, pessoas = 14
        inteiro = total_consumo // total_pessoas                # 186 // 14 = 13
        resto = total_consumo % total_pessoas                   # Resto = 4
        decimal = (resto * 100) // total_pessoas                # (4 * 100) // 14 = 28
        
        # O :02d garante que o decimal tenha sempre 2 dígitos (ex: 5 vira "05")
        print(f"Consumo medio: {inteiro}.{decimal:02d} m3.")
        
        cidade_num += 1

if __name__ == "__main__":
    main()