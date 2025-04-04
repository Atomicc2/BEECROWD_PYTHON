'''
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada
Quatro números inteiros representando a hora de início e fim do jogo.

Saída
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .
'''

a1, b1, a2, b2 = map(int, input().split())

inicio = a1 * 60 + b1
final = a2 * 60 + b2

if final > inicio:
    total = final - inicio
else:
    total = (24 * 60 - inicio) + final

horas = total // 60
minutos = total % 60

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
