def digitize(n):
    nums = [int(i) for i in str(n)]
    return nums[::-1]

print(digitize(35231))