###################################################
# Fibonacci (en récursif)
def fibonacci_recur(n):
    if n == 2 or n == 1:
        return 1
    return fibonacci_recur(n-1) + fibonacci_recur(n-2)

print(fibonacci_recur(3))
###################################################
# Fibonacci (en itératif)
def fibonacci_ite(n):
    x1, x2 = 0, 1
    for i in range(0, n):
        x1, x2 = x2, x1 + x2
    return x1
    
print(fibonacci_ite(17))