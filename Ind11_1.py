def fib(n):
    a,b = 1,1
    for i in range(n):
        yield a
        a,b = b,a + b

count = 1
for num in fib(500):
    print(f"Число №{count} = {num}")
    count += 1

