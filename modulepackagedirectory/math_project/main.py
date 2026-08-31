from mathutils.basic import add, subtract, multiply
from mathutils.number import prime, palindrome, armstrong
from mathutils.statistics import mean, maximum, minimum

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

numbers = [10, 20, 30, 40, 50]

print("Addition:", add(a, b))
print("Subtraction:", subtract(a, b))
print("Multiplication:", multiply(a, b))

print("Prime:", prime(a))
print("Palindrome:", palindrome(a))
print("Armstrong:", armstrong(a))

print("Mean:", mean(numbers))
print("Maximum:", maximum(numbers))
print("Minimum:", minimum(numbers))