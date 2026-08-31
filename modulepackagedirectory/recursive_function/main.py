from recursive import factorial, fibonacci, sum_digits, binary

n = int(input("Enter a number: "))

print("Factorial:", factorial(n))
print("Sum of digits:", sum_digits(n))

print("Fibonacci series:")
for i in range(n):
    print(fibonacci(i), end=" ")

print("\nBinary:", binary(n))