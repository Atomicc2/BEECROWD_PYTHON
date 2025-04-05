#Organizando as entradas de dados

diaInicio = int(input().split()[1])
tempoInicio = list(map(int, input().split(' : ')))
diaFim = int(input().split()[1])
tempoFim = list(map(int, input().split(' : ')))

inicio = (diaInicio * 86400) + (tempoInicio[0] * 3600) + (tempoInicio[1] * 60) + tempoInicio[2]
fim = (diaFim * 86400) + (tempoFim[0] * 3600) + (tempoFim[1] * 60) + tempoFim[2]

total = fim - inicio

dias = total // 86400
total %= 86400
horas = total // 3600
total %= 3600
minutos = total // 60
segundos = total % 60

print(f'{dias} dia(s)')
print(f'{horas} hora(s)')
print(f'{minutos} minuto(s)')
print(f'{segundos} segundo(s)')
