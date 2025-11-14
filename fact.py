def factorial(n):
    # Base condition
    if n == 0 or n == 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)

# Driver code
num = 5
print("Factorial of", num, "is", factorial(num))
