print("=========================================================")
print("===          РИМСКИЙ КАЛЬКУЛЯТОР                ===")
print("=========================================================")
sym = ['I','V','X','L','C','D','M']
va  = [1,5,10,50,100,500,1000]
def rt_o(s):
    s = s.upper().strip()
    if not s:
        return 0
    total = 0
    left  = 0
    right = 1
    while left < len(s):
        if s[left] not in sym:
            return "Ошибка: символ " + s[left] + " не римская цифра"
        cur = va[sym.index(s[left])]
        if right < len(s):
            if s[right] not in sym:
                return "Ошибка: символ " + s[right] + " не римская цифра"
            nxt = va[sym.index(s[right])]
            if cur < nxt:
                total -= cur
            else:
                total += cur
        else:
            total += cur
        left  += 1
        right += 1
    return total
res = []
while True:
    u_input = input("Введите римское число:")
    if u_input.strip() == "":
        break
    ans = rt_o(u_input)
    res.append(ans)
print("Результаты:",res)
