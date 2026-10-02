h = list(input().lower())
j = []
for m in h:
    n = 0
    for k in j:
        if k[0] == m:
            k[1] += 1
            n = 1
            break
    if not n:
        j.append([m, 1])
l = []
for m, v in j:
    l.append([m, v])
    for x in range(len(l) - 1, 0, -1):
        if l[x][1] > l[x-1][1]:
            l[x], l[x-1] = l[x-1], l[x]
            
    if len(l) > 3:
        l = l[:3]
print(l)