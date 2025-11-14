def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)

# Driver code
num = 7
print("Fibonacci series:")
for i in range(num):
    print(fibonacci(i), end=" ")
