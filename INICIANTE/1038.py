'''Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.



Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.'''

def main(item, quantidade):
    lanches = {
        1: 4,
        2: 4.5,
        3: 5,
        4: 2, 
        5: 1.5,
    }
    valor = lanches[item] * quantidade
    print(f"Total: R$ {valor:.2f}")

item, quantidade = map(int, input().split())
main(item, quantidade)