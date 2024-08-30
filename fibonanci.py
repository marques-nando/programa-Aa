def is_fibonacci_number(n):
    if n < 0:
     return False

    # Inicializa os primeiros números da sequência de Fibonacci
    a, b = 0, 1
    
    # Verifica se o número informado é 0 ou 1
    if n == 0 or n == 1:
        return True
    
    # Gera a sequência de Fibonacci até o número informado ou até ultrapassar
    while b < n:
        a, b = b, a + b
    
    # Verifica se o número informado é igual ao último número gerado
    return b == n

# Entrada do usuário
num = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

if is_fibonacci_number(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} NÃO pertence à sequência de Fibonacci.")