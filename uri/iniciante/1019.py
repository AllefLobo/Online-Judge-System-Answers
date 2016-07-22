
tempo = int(input())

hora = 0
minuto = 0
segundo = 0

while 3600< tempo:
    tempo = tempo - 3600
    hora = hora + 1

while 60 < tempo:
    tempo = tempo - 60
    minuto = minuto + 1

segundo = tempo

print "%d:%d:%d" %(hora, minuto, segundo)
