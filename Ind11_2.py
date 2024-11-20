def fib(n):
    a,b = 1,1
    for i in range(n):
        yield a
        a,b = b,a + b

count = 1

with open('fib.txt', 'w') as file:
    for num in fib(500):
        file.write(f'{num}\n')
        count += 1
file.close()
