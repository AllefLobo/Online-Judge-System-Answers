
def fib(n):
    f = [0] * n
    if n <= 2:
        return n
    else:
        f[0] = 0
        f[1] = 1
        for i in range(2,n+1):
            f[i] = f[i - 1] + f[i - 2]
        return f[n]

n = int (input())
print "fib(%d) e %d" %(n, fib(n) )





#fib(5) = 14 calls = 5
