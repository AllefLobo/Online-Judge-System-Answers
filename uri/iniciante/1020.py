
idade = int(input())

ano = 0
mes = 0
dia = 0

while 365 <= idade:
    idade = idade - 365
    ano = ano + 1

while 30 <= idade:
    idade = idade - 30
    mes = mes + 1

dia = idade

print "%d ano(s)" %(ano)
print "%d mes(es)" %(mes)
print "%d dia(s)" %(dia)
