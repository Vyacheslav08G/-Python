def s(n):
    prime = []
    i = 0
    while i <= n:
        prime.append(1)
        i = i + 1
    prime[0] = 0
    prime[1] = 0
    i = 2
    while i <= n:
        if prime[i] == 1:
            j = i * i
            while j <= n:
                prime[j] = 0
                j = j + i
        i = i + 1
    primes = []
    k = 2
    while k <= n:
        if prime[k] == 1:
            primes.append(k)
        k = k + 1
    return primes
N = int(input())
res = s(N)
print("Ищем простые числа в диапазоне от 2 до",N)
print("Простые числа:",res)
