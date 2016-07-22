#include <stdio.h>
int soma = 0;

int fib(int n){
  soma = soma + 1;
  if (n == 0) {
    return 0;
  }else if (n == 1) {
    return 1;
  }else{
    return fib(n-1) + fib(n-2);
  }
}

int main() {
  int n, x;
  scanf("%d\n", &n);
  for (int i = 0; i <= n; i++) {
    n = n -1;
    scanf("%d", &x);
    soma = 0;
    int valor = fib(x);
    printf("fib(%d) = %d calls = %d\n", x, valor, soma -1 );
  }
  return 0;
}
