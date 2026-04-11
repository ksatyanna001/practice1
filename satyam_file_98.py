def feb(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b
n = int(input("Enter the number of Fibonacci numbers to generate: "))   
for num in feb(n):
    print(num)