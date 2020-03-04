def fibonacci_of(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci_of(n-1) + fibonacci_of(n-2)

for i in range(1,201):
    print(fibonacci_of(i))