
a, b, c = map( int, raw_input().split() )

maiorAB = (a + b + abs(a - b) ) / 2
maiorABC = (maiorAB + c + abs(maiorAB - c) ) / 2

print "%d eh o maior" %(maiorABC)
