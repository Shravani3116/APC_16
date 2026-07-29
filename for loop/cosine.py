x = float(input("Enter x: "))
n = int(input("Enter n: "))
sum = 0
for i in range(0, n + 1, 2):
    fact = 1

    for j in range(1, i + 1):
        fact = fact * j

    term = (x ** i) / fact

    if (i // 2) % 2 == 0:
        sum = sum + term
    else:
        sum = sum - term

print("Cosine =", sum)