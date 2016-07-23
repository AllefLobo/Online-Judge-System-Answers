
codigo, qtd = map( int, raw_input().split())

tabela = {1:4.00, 2:4.50, 3:5.00, 4:2.00, 5:1.50}

print "Total: R$ %.2f" %(tabela[codigo] * qtd)
