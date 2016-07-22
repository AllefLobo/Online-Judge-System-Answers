
codigo1, numero1,valor1 = map( float, raw_input().split())

codigo2, numero2,valor2 = map( float, raw_input().split())

total = (numero1 * valor1) + (numero2 * valor2)

print "VALOR A PAGAR: R$ %.2f" %(total)
