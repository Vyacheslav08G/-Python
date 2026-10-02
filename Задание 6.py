def counts(x):
    total = 0
    length = 1
    s = 1
    while s <= x:
        end = min(x, s * 10 - 1)
        total += (end - s + 1) * length
        s *= 10
        length += 1
    return total
def fd(n):
    left = 1
    right = 10**9 + 1
    num = 1
    while left <= right:
        mid = (left + right) // 2
        if counts(mid) >= n:
            num = mid
            right = mid - 1
        else:
            left = mid + 1
    b = counts(num - 1)
    index = n - b - 1
    return int(str(num)[index])
n = int(input())
print([fd(n)])
