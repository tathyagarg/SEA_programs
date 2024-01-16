# Program to find the sum of digits of a number
n = int(input("Enter n: "))
total = 0
while n != 0:
    remainder = n % 10
    total += remainder
    n //= 10
print(total)

