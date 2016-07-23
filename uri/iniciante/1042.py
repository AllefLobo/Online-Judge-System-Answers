

def bublesort():
    global valor
    for i in range(len(valor)):
        for j in range(len(valor)):
            if valor[i] < valor[j] :
                temp = valor[i]
                valor[i] = valor[j]
                valor[j] = temp



valor = map( int, raw_input().split() )
antigo = [ valor[0], valor[1] , valor[2] ]
bublesort()

print valor[0]
print valor[1]
print valor[2]
print ""
print antigo[0]
print antigo[1]
print antigo[2]
