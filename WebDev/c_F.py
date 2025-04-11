x = int(input())
reversed_number = 0

while x > 0:
    reversed_number = reversed_number * 10 + x % 10
    x //= 10

print(reversed_number)
