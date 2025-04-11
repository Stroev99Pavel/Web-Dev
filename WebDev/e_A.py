def find_min(a, b, c, d):
    smallest = a
    if b < smallest:
        smallest = b
    if c < smallest:
        smallest = c
    if d < smallest:
        smallest = d

    return smallest

a, b, c, d = map(int, input().split())

print(find_min(a, b, c, d))
