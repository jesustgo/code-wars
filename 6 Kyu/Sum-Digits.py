def digital_root(n):
    while n >= 10:
        digit = n % 10
        n = n // 10
        n = digit + n
    return n

print(digital_root(639892698300695830))