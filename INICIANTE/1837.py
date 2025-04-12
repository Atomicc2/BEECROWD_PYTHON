def divisao_euclidiana(a, b):
    """
    Calcula o quociente e o resto segundo o Teorema da Divisão Euclidiana.
    
    Args:
        a: dividendo (número inteiro)
        b: divisor (número inteiro não-nulo)
        
    Returns:
        q: quociente (número inteiro)
        r: resto (número inteiro tal que 0 <= r < |b|)
    """
    # Verificação do divisor
    if b == 0:
        raise ValueError("O divisor não pode ser zero")
    
    # Calculando quociente e resto
    q = a // abs(b)  # Divisão inteira pelo valor absoluto de b
    r = a - abs(b) * q
    
    # Ajustando para garantir que 0 <= r < |b|
    if r < 0:
        r += abs(b)
        q -= 1 if b > 0 else -1
    
    # Se b for negativo, ajustamos o sinal do quociente
    if b < 0:
        q = -q
        
    return q, r

# Entrada dos valores
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

try:
    # Calculando quociente e resto
    q, r = divisao_euclidiana(a, b)
    
    # Imprimindo o resultado
    print(q, r)
    
except ValueError as e:
    print(f"Erro: {e}")