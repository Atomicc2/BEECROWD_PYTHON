codigo_a, quantidade_a, valor_a = input().split()
codigo_b, quantidade_b, valor_b = input().split()

codigo_a = int(codigo_a)
quantidade_a = int(quantidade_a)
valor_a = float(valor_a)

codigo_b = int(codigo_b)
quantidade_b = int(quantidade_b)
valor_b = float(valor_b)

soma_a = quantidade_a * valor_a
soma_b = quantidade_b * valor_b

total = soma_a + soma_b
print(f"VALOR A PAGAR = R$ {total:.2f}")