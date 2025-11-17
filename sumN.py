def sum_of_digits(n):
    # Base case
    if n == 0:
        return 0
    # Recursive case
    return (n % 10) + sum_of_digits(n // 10)


num = 9875
print("Sum of digits of", num, "is:", sum_of_digits(num))
